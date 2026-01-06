import numpy as np
import pandas as pd
import data_generator as dg
from datetime import datetime

def get_season(month: int) -> str:
    if month in (12, 1, 2):
        return "Winter"
    elif month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    else:
        return "Fall"

class InventorySimulator:

    def __init__(self, start_date, end_date, random_seed=42):

        self.rng = np.random.default_rng(random_seed)
        self.start_date = pd.to_datetime(start_date)
        self.end_date = pd.to_datetime(end_date)
        self.dim_date = self.build_dim_date()
        self.seasonal = dg.create_seasons()
        self.stores = dg.create_stores(random_seed)
        self.vendors = dg.generate_vendors(self.stores, self.rng)

        self.vendor_store_eligibility = dg.build_vendor_store_eligibility(
            self.stores,
            self.vendors
        )

    def build_dim_date(self):
        dates = pd.date_range(self.start_date, self.end_date, freq="D")
        df = pd.DataFrame({"date": dates})
        df["date_id"] = df["date"].dt.strftime("%Y%m%d").astype(int)
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        df["day"] = df["date"].dt.day
        df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)
        df["day_of_week"] = df["date"].dt.dayofweek  # 0=Mon, 6=Sun
        df["is_weekend"] = df["day_of_week"].isin([5, 6])
        df["season"] = df["month"].apply(get_season)
        return df

    def build_holiday_weeks(self):
        holidays = [
        {"name": "New Year's Day", "month": 1, "day": 1},
        {"name": "Valentine's Day", "month": 2, "day": 14},
        {"name": "Independence Day", "month": 7, "day": 4},
        {"name": "Halloween", "month": 10, "day": 31},
        {"name": "Christmas Day", "month": 12, "day": 25},
        {"name": "Super Bowl", "month": 2, "day": 10},
        {"name": "Memorial Day", "month": 5, "day": 27},
        {"name": "Labor Day", "month": 9, "day": 2},
        {"name": "Easter Sunday", "month": 3, "day": 31},
        {"name": "Thanksgiving", "month": 11, "day": 28},
    ]

        week_df = self.dim_date[["year", "week_of_year"]].drop_duplicates().copy()
        week_df["week_factor"] = 1.0
        week_df["holiday_name"] = ""

        for h in holidays:
            mask = (self.dim_date["month"] == h["month"]) & (self.dim_date["day"] == h["day"])
            holiday_dates = self.dim_date[mask]

            for _, row in holiday_dates.iterrows():
                y = row["year"]
                w = row["week_of_year"]

                prior_w = w - 1
                next_w = w + 1

                up = 1.0 + self.rng.uniform(0.01, 0.10)
                down = 1.0 - self.rng.uniform(0.01, 0.05)

                idx = (week_df["year"] == y) & (week_df["week_of_year"] == w)
                week_df.loc[idx, "week_factor"] *= up
                name_mask = idx & (week_df["holiday_name"] == "")
                week_df.loc[name_mask, "holiday_name"] = h["name"]

                idx_prev = (week_df["year"] == y) & (week_df["week_of_year"] == prior_w)
                week_df.loc[idx_prev, "week_factor"] *= up

                idx_next = (week_df["year"] == y) & (week_df["week_of_year"] == next_w)
                week_df.loc[idx_next, "week_factor"] *= down

        return week_df

    def vendor_weekly_lambda(self, category, size):
        category = str(category).strip().lower()
        size = str(size).strip().lower()

        if category == "snacks":
            return 2.0 if size == "large" else 0.3

        base_by_category = {
            "beverages": 3.0,
            "dairy": 4.0,
            "frozen": 0.5,
            "liquor": 1.0,
            "bread": 5.0,
            "produce": 5.0,
        }

        return base_by_category.get(category, 1.0)


    def generate_delivery_schedule(self):
        pairs = (
            self.vendor_store_eligibility
                .merge(
                    self.vendors[
                        ["vendor_id", "vendor_size", "vendor_category", "coverage_type"]
                    ],
                    on="vendor_id",
                    how="left"
                )
        )

        pairs = pairs[["store_id", "vendor_id", "vendor_size", "vendor_category"]].copy()
        coverage_lambda_mult = {
            "national": 1.00,
            "region":   0.45,
            "state":    0.25,
        }
        pairs["base_lambda"] = pairs.apply(
            lambda r: self.vendor_weekly_lambda(r["vendor_category"], r["vendor_size"]),
            axis=1,
        )

        pairs["weekly_lambda"] = pairs.apply(
            lambda r: self.vendor_weekly_lambda(r["vendor_category"], r["vendor_size"]),
            axis=1,
        )

        store_vendor_array = pairs[["store_id", "vendor_id"]].to_numpy()
        lambda_array = pairs["weekly_lambda"].to_numpy()

        holiday_weeks = self.build_holiday_weeks().set_index(["year", "week_of_year"])

        deliveries = []

        for (year, week), week_dates in self.dim_date.groupby(["year", "week_of_year"]):
            week_dates = week_dates.sort_values("date")
            n_days = len(week_dates)
            if n_days == 0:
                continue

            key = (year, week)
            if key in holiday_weeks.index:
                factor = float(holiday_weeks.loc[key, "week_factor"])
            else:
                factor = 1.0

            base_weights = np.where(week_dates["is_weekend"], 0.3, 1.0)
            prob = base_weights / base_weights.sum()
            date_ids = week_dates["date_id"].to_numpy()

            lambda_effective = lambda_array * factor
            counts = self.rng.poisson(lambda_effective)
            counts = np.clip(counts, 0, n_days)

            rows = []

            for idx, k in enumerate(counts):
                if k == 0:
                    continue

                chosen_idx = self.rng.choice(n_days, size=k, replace=False, p=prob)
                chosen_dates = date_ids[chosen_idx]

                store_id, vendor_id = store_vendor_array[idx]

                rows.append(
                    pd.DataFrame(
                        {
                            "store_id": np.full(k, store_id, dtype=int),
                            "vendor_id": np.full(k, vendor_id, dtype=int),
                            "date_id": chosen_dates.astype(int),
                        }
                    )
                )

            if rows:
                deliveries.append(pd.concat(rows, ignore_index=True))

        if deliveries:
            schedule_df = pd.concat(deliveries, ignore_index=True)
        else:
            schedule_df = pd.DataFrame(
                {
                    "store_id": pd.Series(dtype="int64"),
                    "vendor_id": pd.Series(dtype="int64"),
                    "date_id": pd.Series(dtype="int64"),
                }
            )

        return schedule_df

    def generate_metrics(self, schedule_df):

        df = schedule_df.copy()

        store_cols = [
            "store_id",
            "city",
            "state",
            "ordering_size",
            "region",
            "dairy_mult",
            "frozen_food_mult",
            "fresh_produce_mult",
            "beverages_mult",
            "liquor_mult",
            "bread_mult",
            "snacks_mult",
        ]

        df = df.merge(self.stores[store_cols], on="store_id", how="left")

        df = df.merge(
            self.vendors[["vendor_id", "vendor_name", "vendor_size", "vendor_category"]],
            on="vendor_id",
            how="left"
        )

        df = df.merge(
            self.dim_date[["date_id", "date", "month", "season"]],
            on="date_id",
            how="left"
        )

        df = df.merge(
            self.seasonal,
            on=["region", "season"],
            how="left"
        )

        conds = [
            df["vendor_category"].eq("dairy"),
            df["vendor_category"].eq("produce"),
            df["vendor_category"].eq("frozen"),
            df["vendor_category"].eq("liquor"),
            df["vendor_category"].eq("bread"),
            df["vendor_category"].eq("snacks"),
            df["vendor_category"].eq("beverages"),
        ]

        base_choices = [
            df["dairy_mult"],
            df["fresh_produce_mult"],
            df["frozen_food_mult"],
            df["liquor_mult"],
            df["bread_mult"],
            df["snacks_mult"],
            df["beverages_mult"],
        ]

        seasonal_choices = [
            df["dairy_season_mult"],
            df["fresh_produce_season_mult"],
            df["frozen_food_season_mult"],
            df["liquor_season_mult"],
            df["bread_season_mult"],
            df["snacks_season_mult"],
            df["beverages_season_mult"],
        ]

        df["category_base_mult"] = np.select(conds, base_choices, default=1.0)
        df["category_season_mult"] = np.select(conds, seasonal_choices, default=1.0)

        df["demand_scale"] = (df["ordering_size"] * df["category_base_mult"] * df["category_season_mult"])

        size_to_lambda = {"small": 5, "medium": 17, "large": 30}
        df["lambda_sku"] = df["vendor_size"].map(size_to_lambda).fillna(15)

        df["lambda_sku_adj"] = (df["lambda_sku"] * df["demand_scale"]).clip(lower=1)

        category_sku_factor = {
            "liquor": 0.5,
            "frozen": 0.8,
            "produce": 0.5
        }

        df["sku_lambda_factor"] = df["vendor_category"].map(category_sku_factor).fillna(1.0)
        df["lambda_sku_final"] = (df["lambda_sku_adj"] * df["sku_lambda_factor"]).clip(lower=1)

        df["sku_count"] = self.rng.poisson(lam=df["lambda_sku_final"].values).clip(min=1)

        base_qty = self.rng.integers(2, 20, size=len(df))
        df["category_item_factor"] = df["vendor_category"].map({
                "liquor": 0.4,
                "bread": 0.5, 
       }).fillna(1.0)

        df["base_qty_effective"] = (base_qty * df["category_item_factor"]).round().clip(lower=1)

        df["total_items"] = (
            df["sku_count"] * df["base_qty_effective"] * df["demand_scale"]
        ).round().clip(lower=1).astype(int)

        price_ranges = {
            "bread": (2.50, 5.50),
            "dairy": (1.50, 5.00),
            "frozen": (1.00, 9.00),
            "produce": (0.30, 4.00),
            "liquor": (8.00, 10.00),
            "beverages": (2.00, 11.00),
            "snacks": (0.50, 7.00),
        }

        min_price_map = {k: v[0] for k, v in price_ranges.items()}
        max_price_map = {k: v[1] for k, v in price_ranges.items()}

        min_price = df["vendor_category"].map(min_price_map).fillna(2.0)
        max_price = df["vendor_category"].map(max_price_map).fillna(10.0)

        qty = df["total_items"].astype(float).values
        qty_norm = np.log(qty + 1.0)
        qty_norm = (qty_norm - qty_norm.min()) / (qty_norm.max() - qty_norm.min() + 1e-6)

        price_pos = 1.0 - qty_norm
        price_pos = price_pos + self.rng.normal(loc=0.0, scale=0.15, size=len(df))
        price_pos = np.clip(price_pos, 0.0, 1.0)

        unit_price = min_price + price_pos * (max_price - min_price)



        df["avg_unit_price"] = unit_price.round(2)
        df["invoice_amount"] = (df["avg_unit_price"] * df["total_items"]).round(2)
        base_time = 90
        alpha = 30
        noise = self.rng.normal(loc=0, scale=60, size=len(df))

        raw_seconds = (base_time + alpha * np.log(df["total_items"] + 1) + noise)

        window_seconds = 8 * 3600  # 6am–2pm
        df["time_seconds"] = np.clip(raw_seconds, 60, window_seconds).round().astype(int)

        available = np.maximum(window_seconds - df["time_seconds"], 0)
        start_offsets = self.rng.integers(0, available + 1)

        base_start = df["date"] + pd.to_timedelta(6, unit="h")
        df["invoice_initiated_ts"] = base_start + pd.to_timedelta(start_offsets, unit="s")
        df["invoice_finished_ts"] = df["invoice_initiated_ts"] + pd.to_timedelta(df["time_seconds"], unit="s")

        df = df.reset_index(drop=True)
        df["transaction_id"] = df.index + 1

        fact_cols = [
            "transaction_id",
            "store_id",
            "city",
            "state",
            "region",
            "vendor_id",
            "vendor_name",
            "vendor_category",
            "date_id",
            "date",
            "sku_count",
            "total_items",
            "invoice_amount",
            "vendor_size",
            "invoice_initiated_ts",
            "invoice_finished_ts",
        ]
        return df[fact_cols]

    def run(self):
        schedule_df = self.generate_delivery_schedule()
        fact_df = self.generate_metrics(schedule_df)
        return fact_df


sim_2024_2025 = InventorySimulator(
    start_date="2024-01-01",
    end_date="2025-09-30",
    random_seed=67,
)

fact_2024_2025 = sim_2024_2025.run()



fact_2024_2025.to_csv("2024_2025_national_vendor_invoices.csv", index=False)

print("saved 2024_2025_national_vendor_invoices.csv")
