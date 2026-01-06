import pandas as pd

df = pd.read_csv("2024_national_vendor_invoices.csv")
df.to_parquet("2024_national_vendor_invoices.parquet", index=False)
print("2024 successfully converted to parquet")

df = pd.read_csv("2025_national_vendor_invoices.csv")
df.to_parquet("2025_national_vendor_invoices.parquet", index=False)

print("2025 successfully converted to parquet")
