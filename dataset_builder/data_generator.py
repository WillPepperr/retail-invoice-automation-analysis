import pandas as pd 
import numpy as np


def create_stores(seed=667):
    df = pd.read_csv("Sheets/us_cities_top_500.csv")

    df["population"] = (
        df["population"].astype(str).str.replace(",", "", regex=False).astype(int)
    )

    total_pop = df["population"].sum()
    df["weight"] = df["population"] / total_pop

    num_stores = 290


    sampled_rows = df.sample(
        n=num_stores,
        replace=True,
        weights="weight",
        random_state=seed,
    )

    stores_df = pd.DataFrame({
        "store_id": range(1, num_stores + 1),
        "city": sampled_rows["city"].values,
        "state": sampled_rows["state"].values
    })

    np.random.seed(seed) 

    stores_df["ordering_size"] = np.random.triangular(0.8, 1.2, 1.4, size=num_stores)

    state_to_region = {
        # Midwest
        "Illinois": "Midwest",
        "Iowa": "Midwest",
        "Ohio": "Midwest",
        "Michigan": "Midwest",
        "Indiana": "Midwest",
        "Wisconsin": "Midwest",
        "Minnesota": "Midwest",
        "Missouri": "Midwest",
        "Kansas": "Midwest",
        "Nebraska": "Midwest",
        "South Dakota": "Midwest",
        "North Dakota": "Midwest",

        # Northeast
        "New York": "Northeast",
        "New Jersey": "Northeast",
        "Pennsylvania": "Northeast",
        "Massachusetts": "Northeast",
        "Connecticut": "Northeast",
        "Rhode Island": "Northeast",
        "New Hampshire": "Northeast",
        "Vermont": "Northeast",
        "Maine": "Northeast",

        # South
        "Texas": "South",
        "Florida": "South",
        "Georgia": "South",
        "Alabama": "South",
        "Mississippi": "South",
        "Louisiana": "South",
        "South Carolina": "South",
        "North Carolina": "South",
        "Virginia": "South",
        "West Virginia": "South",
        "Tennessee": "South",
        "Kentucky": "South",
        "Arkansas": "South",
        "Oklahoma": "South",
        "Maryland": "South",
        "Delaware": "South",

        # West
        "California": "West",
        "Nevada": "West",
        "Washington": "West",
        "Oregon": "West",
        "Arizona": "West",
        "Colorado": "West",
        "Utah": "West",
        "Idaho": "West",
        "Montana": "West",
        "Wyoming": "West",
        "New Mexico": "West",

    }



    # Add region to each store
    stores_df["region"] = stores_df["state"].map(state_to_region)


    region_industry_prefs = pd.DataFrame([
        {
            "region": "Midwest",
            "dairy_mult": 1.25,
            "frozen_food_mult": 1.14,
            "fresh_produce_mult": 0.83,
            "beverages_mult": 1.00,
            "liquor_mult": 1.34,
            "bread_mult": 1.11,
            "snacks_mult": 1.17,
        },
        {
            "region": "Northeast",
            "dairy_mult": 1.29,
            "frozen_food_mult": 1.30,  
            "fresh_produce_mult": .92,
            "beverages_mult": 1.05,
            "liquor_mult": 1.30,
            "bread_mult": 1.12,
            "snacks_mult": 1.17,
        },
        {
            "region": "South",
            "dairy_mult": 0.94,
            "frozen_food_mult": 0.84,
            "fresh_produce_mult": 1.25,
            "beverages_mult": 1.20,
            "liquor_mult": .85,
            "bread_mult": 0.97,
            "snacks_mult": 1.24,
        },
        {
            "region": "West",
            "dairy_mult": 0.87,
            "frozen_food_mult": 0.95,
            "fresh_produce_mult": 1.40, 
            "beverages_mult": 1.05,
            "liquor_mult": 1.00,
            "bread_mult": 0.89,
            "snacks_mult": 0.98,
        },
    ])

    stores_df = stores_df.merge(region_industry_prefs, on="region", how="left")

    return stores_df

def create_seasons():
    seasonal_multipliers = pd.DataFrame([
        # MIDWEST
        {"region": "Midwest", "season": "Winter",
         "frozen_food_season_mult": 1.20,
         "dairy_season_mult": 0.90,
         "fresh_produce_season_mult": 0.80,
         "beverages_season_mult": 0.95,
         "liquor_season_mult": 1.15,
         "bread_season_mult": 1.05,
         "snacks_season_mult": 1.10},
        
        {"region": "Midwest", "season": "Summer",
         "frozen_food_season_mult": 0.85,
         "dairy_season_mult": 1.20,
         "fresh_produce_season_mult": 1.25,
         "beverages_season_mult": 1.15,
         "liquor_season_mult": 1.00,
         "bread_season_mult": 0.95,
         "snacks_season_mult": 1.05},
    
        {"region": "Midwest", "season": "Spring",
         "frozen_food_season_mult": 0.95,
         "dairy_season_mult": 1.05,
         "fresh_produce_season_mult": 1.20,
         "beverages_season_mult": 1.05,
         "liquor_season_mult": 1.00,
         "bread_season_mult": 1.00,
         "snacks_season_mult": 1.05},
    
        {"region": "Midwest", "season": "Fall",
         "frozen_food_season_mult": 1.05,
         "dairy_season_mult": 1.00,
         "fresh_produce_season_mult": 0.90,
         "beverages_season_mult": 0.95,
         "liquor_season_mult": 1.20,
         "bread_season_mult": 1.10,
         "snacks_season_mult": 1.15},
    
        # SOUTH
        {"region": "South", "season": "Winter",
         "frozen_food_season_mult": 1.05,
         "dairy_season_mult": 1.00,
         "fresh_produce_season_mult": 1.10,
         "beverages_season_mult": 1.15,
         "liquor_season_mult": 1.10,
         "bread_season_mult": 1.00,
         "snacks_season_mult": 1.10},
    
        {"region": "South", "season": "Summer",
         "frozen_food_season_mult": 0.80,
         "dairy_season_mult": 1.25,
         "fresh_produce_season_mult": 1.35,
         "beverages_season_mult": 1.25,
         "liquor_season_mult": 0.90,
         "bread_season_mult": 0.90,
         "snacks_season_mult": 1.05},
    
        {"region": "South", "season": "Spring",
         "frozen_food_season_mult": 0.95,
         "dairy_season_mult": 1.05,
         "fresh_produce_season_mult": 1.30,
         "beverages_season_mult": 1.10,
         "liquor_season_mult": 1.00,
         "bread_season_mult": 0.95,
         "snacks_season_mult": 1.10},
    
        {"region": "South", "season": "Fall",
         "frozen_food_season_mult": 0.90,
         "dairy_season_mult": 1.00,
         "fresh_produce_season_mult": 1.10,
         "beverages_season_mult": 1.00,
         "liquor_season_mult": 1.20,
         "bread_season_mult": 1.05,
         "snacks_season_mult": 1.20},
        
    
        # WEST
        {"region": "West", "season": "Winter",
         "frozen_food_season_mult": 1.00,
         "dairy_season_mult": 0.95,
         "fresh_produce_season_mult": 1.20,
         "beverages_season_mult": 1.05,
         "liquor_season_mult": 1.10,
         "bread_season_mult": 0.95,
         "snacks_season_mult": 1.00},
    
        {"region": "West", "season": "Summer",
         "frozen_food_season_mult": 0.90,
         "dairy_season_mult": 1.20,
         "fresh_produce_season_mult": 1.40,
         "beverages_season_mult": 1.15,
         "liquor_season_mult": 1.00,
         "bread_season_mult": 0.90,
         "snacks_season_mult": 0.95},
    
        {"region": "West", "season": "Spring",
         "frozen_food_season_mult": 0.95,
         "dairy_season_mult": 1.05,
         "fresh_produce_season_mult": 1.30,
         "beverages_season_mult": 1.10,
         "liquor_season_mult": 1.00,
         "bread_season_mult": 0.95,
         "snacks_season_mult": 1.00},
    
        {"region": "West", "season": "Fall",
         "frozen_food_season_mult": 1.00,
         "dairy_season_mult": 0.95,
         "fresh_produce_season_mult": 1.10,
         "beverages_season_mult": 1.00,
         "liquor_season_mult": 1.20,
         "bread_season_mult": 1.00,
         "snacks_season_mult": 1.05},
    
        # NORTHEAST
        {"region": "Northeast", "season": "Winter",
         "frozen_food_season_mult": 1.25,
         "dairy_season_mult": 0.92,
         "fresh_produce_season_mult": 0.85,
         "beverages_season_mult": 1.00,
         "liquor_season_mult": 1.20,
         "bread_season_mult": 1.15,
         "snacks_season_mult": 1.10},
        
        {"region": "Northeast", "season": "Summer",
         "frozen_food_season_mult": 1.10,
         "dairy_season_mult": 1.05,
         "fresh_produce_season_mult": 1.20,
         "beverages_season_mult": 1.25,
         "liquor_season_mult": 1.05,
         "bread_season_mult": 0.95,
         "snacks_season_mult": 1.10},
        
        {"region": "Northeast", "season": "Spring",
         "frozen_food_season_mult": 1.00,
         "dairy_season_mult": 1.10,
         "fresh_produce_season_mult": 1.15,
         "beverages_season_mult": 1.10,
         "liquor_season_mult": 1.00,
         "bread_season_mult": 1.00,
         "snacks_season_mult": 1.05},
        
        {"region": "Northeast", "season": "Fall",
         "frozen_food_season_mult": 1.05,
         "dairy_season_mult": 1.00,
         "fresh_produce_season_mult": 1.25,
         "beverages_season_mult": 1.05,
         "liquor_season_mult": 1.25,
         "bread_season_mult": 1.10,
         "snacks_season_mult": 1.15},
    ])
    return seasonal_multipliers




def generate_vendors(stores, rng) -> pd.DataFrame:

    national_vendors = [
        # snacks
        {"vendor_name": "Frito-Lay", "vendor_category": "snacks", "vendor_size": "large"},
        {"vendor_name": "Utz Quality Foods",      "vendor_category": "snacks",    "vendor_size": "medium"},
        {"vendor_name": "Blue Diamond Growers", "vendor_category": "snacks", "vendor_size": "medium"},
        {"vendor_name": "Nabisco:", "vendor_category": "snacks", "vendor_size": "large"},


        # beverages
        {"vendor_name": "Coca-Cola Bottling Co.", "vendor_category": "beverages", "vendor_size": "large"},
        {"vendor_name": "PepsiCo Beverages",      "vendor_category": "beverages", "vendor_size": "large"},
        {"vendor_name": "Keurig Dr.Pepper", "vendor_category": "beverages", "vendor_size": "large"},

        # dairy
        {"vendor_name": "Prairie Farms Dairy",    "vendor_category": "dairy",     "vendor_size": "medium"},
        {"vendor_name": "Dairy Farmers of America","vendor_category":"dairy",     "vendor_size": "large"},
        {"vendor_name": "Oberweis", "vendor_category": "dairy", "vendor_size":"small"},
        {"vendor_name": "Ben & Jerry's (Unilever)", "vendor_category": "dairy", "vendor_size": "large"},
        {"vendor_name": "Blue Bell Creameries", "vendor_category": "dairy", "vendor_size": "medium"},
        {"vendor_name": "Tillamook Ice Cream", "vendor_category": "dairy", "vendor_size": "medium"},
        {"vendor_name": "Haagen-Dazs (Nestlé/General Mills)", "vendor_category": "dairy", "vendor_size": "large"},
        
        # bread
        {"vendor_name": "Bimbo Bakeries USA", "vendor_category": "bread", "vendor_size": "large"},
        {"vendor_name": "Pepperidge Farm (Campbell Soup Co.)", "vendor_category": "bread", "vendor_size": "small"},
        {"vendor_name": "Flowers Foods (Nature's Own, Wonder Bread)", "vendor_category": "bread", "vendor_size": "large"},
        {"vendor_name": "Sara Lee Bread (Bimbo)", "vendor_category": "bread", "vendor_size": "medium"},
        {"vendor_name": "Arnold / Oroweat / Brownberry (Bimbo)", "vendor_category": "bread", "vendor_size": "medium"},
        {"vendor_name": "Dave's Killer Bread (Flowers Foods)", "vendor_category": "bread", "vendor_size": "small"},
        {"vendor_name": "Hostess Brands", "vendor_category": "bread", "vendor_size": "large"},
        {"vendor_name": "Thomas' (Bimbo)", "vendor_category": "bread", "vendor_size": "medium"},
        {"vendor_name": "Einstein Bros Bagels (JAB Holdings)", "vendor_category": "bread", "vendor_size": "medium"},
        {"vendor_name": "King's Hawaiian", "vendor_category": "bread", "vendor_size": "medium"},
        {"vendor_name": "La Brea Bakery (Aryzta)", "vendor_category": "bread", "vendor_size": "small"},

        # frozen
        {"vendor_name": "General Mills Frozen",   "vendor_category": "frozen",    "vendor_size": "medium"},
        {"vendor_name": "Conagra Brands)", "vendor_category": "frozen", "vendor_size": "large"},
        {"vendor_name": "Nestlé USA Frozen", "vendor_category": "frozen", "vendor_size": "large"},
        {"vendor_name": "Kraft Heinz Frozen Division", "vendor_category": "frozen", "vendor_size": "large"},

        {"vendor_name": "Green Giant (B&G Foods)", "vendor_category": "frozen", "vendor_size": "large"},
        {"vendor_name": "Birds Eye (Conagra)", "vendor_category": "frozen", "vendor_size": "large"},

        {"vendor_name": "Gorton's Seafood", "vendor_category": "frozen", "vendor_size": "medium"},
        {"vendor_name": "Trident Seafoods", "vendor_category": "frozen", "vendor_size": "medium"},

        {"vendor_name": "Schwan’s Company", "vendor_category": "frozen", "vendor_size": "large"},
        {"vendor_name": "Nestlé Pizza Division", "vendor_category": "frozen", "vendor_size": "large"},
        {"vendor_name": "Kellogg's Frozen (Eggo)", "vendor_category": "frozen", "vendor_size": "medium"},
        {"vendor_name": "Tyson Foods (Any'tizers)", "vendor_category": "frozen", "vendor_size": "large"},
        {"vendor_name": "McCain Foods (fries, potato snacks)", "vendor_category": "frozen", "vendor_size": "large"},
        {"vendor_name": "Totino’s / Jeno’s (General Mills)", "vendor_category": "frozen", "vendor_size": "medium"},

        # produce
        {"vendor_name": "FreshPoint National",    "vendor_category": "produce",   "vendor_size": "large"},
        {"vendor_name": "FreshPoint National (Sysco)", "vendor_category": "produce", "vendor_size": "large"},
        {"vendor_name": "Sysco Produce Division", "vendor_category": "produce", "vendor_size": "large"},
        {"vendor_name": "US Foods Produce", "vendor_category": "produce", "vendor_size": "large"},
        {"vendor_name": "Taylor Farms", "vendor_category": "produce", "vendor_size": "large"},
        {"vendor_name": "Dole Fresh Vegetables", "vendor_category": "produce", "vendor_size": "large"},
        {"vendor_name": "Chiquita Brands International", "vendor_category": "produce", "vendor_size": "large"},
        {"vendor_name": "Driscoll’s Berries", "vendor_category": "produce", "vendor_size": "medium"},
        {"vendor_name": "Fresh Express (Chiquita)", "vendor_category": "produce", "vendor_size": "large"},
        {"vendor_name": "Mann Packing (Del Monte Fresh)", "vendor_category": "produce", "vendor_size": "medium"},
        {"vendor_name": "Calavo Growers (avocados, fresh packs)", "vendor_category": "produce", "vendor_size": "medium"},


        # liquor
        {"vendor_name": "Southern Glazer's Wine & Spirits", "vendor_category": "liquor", "vendor_size": "large"},
        {"vendor_name": "Republic National Distributing Company (RNDC)", "vendor_category": "liquor", "vendor_size": "large"},
        {"vendor_name": "Breakthru Beverage Group", "vendor_category": "liquor", "vendor_size": "large"},

        {"vendor_name": "Anheuser-Busch InBev (AB One Wholesalers)", "vendor_category": "liquor", "vendor_size": "large"},
        {"vendor_name": "Molson Coors Beverage Company (Coors Distributing)", "vendor_category": "liquor", "vendor_size": "large"},
        {"vendor_name": "Heineken USA Distribution", "vendor_category": "liquor", "vendor_size": "medium"},
        {"vendor_name": "Constellation Brands Beer Division (Modelo, Corona)", "vendor_category": "liquor", "vendor_size": "large"},

        {"vendor_name": "Johnson Brothers Beverage Company", "vendor_category": "liquor", "vendor_size": "medium"},
        {"vendor_name": "Young's Market (Now part of RNDC West)", "vendor_category": "liquor", "vendor_size": "medium"},

        {"vendor_name": "Bell’s Brewery / New Belgium Distribution Network", "vendor_category": "liquor", "vendor_size": "small"},
        {"vendor_name": "Craft Brewers Guild (Sheehan Family Companies)", "vendor_category": "liquor", "vendor_size": "medium"},

    ]
    nat_df = pd.DataFrame(national_vendors)
    nat_df["coverage_type"] = "national"
    nat_df["coverage_region"] = pd.NA
    nat_df["coverage_state"] = pd.NA

    # --- 2) Regional distributors ---
    regions = sorted(stores["region"].unique())
    categories = ["dairy", "produce", "frozen", "liquor", "bread", "snacks", "beverages"]

    regional_records = []
    for region in regions:
        n_reg = rng.integers(2, 4)
        for i in range(n_reg):
            cat = rng.choice(categories)
            size = rng.choice(["small", "medium"], p=[0.6, 0.4])
            regional_records.append({
                "vendor_name": f"{region} {cat.title()} Distributors {i+1}",
                "vendor_category": cat,
                "vendor_size": size,
                "coverage_type": "region",
                "coverage_region": region,
                "coverage_state": pd.NA,
            })
    reg_df = pd.DataFrame(regional_records) if regional_records else pd.DataFrame(
        columns=["vendor_name", "vendor_category", "vendor_size",
                 "coverage_type", "coverage_region", "coverage_state"]
    )

    # --- 3) State-wide distributors ---
    state_col = "state" if "state" in stores.columns else None
    state_df_list = []
    if state_col is not None:
        states = sorted(stores[state_col].unique())
        state_records = []
        for state in states:
            n_state = rng.integers(2, 6)
            for i in range(n_state):
                cat = rng.choice(categories)
                size = rng.choice(["small", "medium"], p=[0.7, 0.3])
                state_records.append({
                    "vendor_name": f"{state} {cat.title()} Supply {i+1}",
                    "vendor_category": cat,
                    "vendor_size": size,
                    "coverage_type": "state",
                    "coverage_region": pd.NA,
                    "coverage_state": state,
                })
        state_df_list.append(pd.DataFrame(state_records))

    state_df = (
        pd.concat(state_df_list, ignore_index=True)
        if state_df_list
        else pd.DataFrame(
            columns=["vendor_name", "vendor_category", "vendor_size",
                     "coverage_type", "coverage_region", "coverage_state"]
        )
    )

    # --- 4) Combine & assign vendor_id ---
    vendors = pd.concat([nat_df, reg_df, state_df], ignore_index=True)

    if vendors.empty:
        vendors = pd.DataFrame([{
            "vendor_name": "Fallback Vendor",
            "vendor_category": "snacks",
            "vendor_size": "medium",
            "coverage_type": "national",
            "coverage_region": pd.NA,
            "coverage_state": pd.NA,
        }])

    vendors.insert(0, "vendor_id", np.arange(1, len(vendors) + 1, dtype="int64"))

    # --- 5) Delivery frequency ---
    size_to_base = {"small": 1.5, "medium": 3.0, "large": 5.0}
    base = vendors["vendor_size"].map(size_to_base).fillna(2.0)
    noise = rng.normal(0, 0.7, size=len(vendors))
    vendors["base_deliveries_per_week"] = (
        base + noise
    ).round().clip(lower=1, upper=7).astype(int)

    # --- 6) Holiday effect ---
    cat_to_holiday_mean = {
        "dairy": 1.15,
        "produce": 1.20,
        "frozen": 1.10,
        "liquor": 1.30,
        "bread": 1.18,
        "snacks": 1.25,
        "beverages": 1.30,
    }

    means = vendors["vendor_category"].map(cat_to_holiday_mean).fillna(1.15)
    holiday_noise = rng.normal(0, 0.03, size=len(vendors))
    vendors["holiday_effect"] = (means + holiday_noise).clip(lower=1.0, upper=1.5)

    cols = [
        "vendor_id",
        "vendor_name",
        "vendor_category",
        "vendor_size",
        "coverage_type",
        "coverage_region",
        "coverage_state",
        "base_deliveries_per_week",
        "holiday_effect",
    ]
    return vendors[cols]


def build_vendor_store_eligibility(stores: pd.DataFrame, vendors: pd.DataFrame) -> pd.DataFrame:
    s = stores[["store_id", "region", "state"]].copy()
    v = vendors[["vendor_id", "coverage_type", "coverage_region", "coverage_state"]].copy()

    # National: cross join all stores
    nat = v.query("coverage_type == 'national'")[["vendor_id"]].merge(
        s[["store_id"]], how="cross"
    )

    # Regional: join on region
    reg = v.query("coverage_type == 'region'")[["vendor_id", "coverage_region"]].merge(
        s, left_on="coverage_region", right_on="region", how="inner"
    )[["vendor_id", "store_id"]]

    # State: join on state
    st = v.query("coverage_type == 'state'")[["vendor_id", "coverage_state"]].merge(
        s, left_on="coverage_state", right_on="state", how="inner"
    )[["vendor_id", "store_id"]]

    return pd.concat([nat, reg, st], ignore_index=True)
