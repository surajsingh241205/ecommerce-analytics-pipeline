import pandas as pd 
df = pd.read_csv("data/raw/olist_geolocation_dataset.csv")

# Inspecting geo location duplicates

# print("Total rows:", len(df))
# print("Exact duplicates:", df.duplicated().sum())

# print("\nDuplicate ZIP codes:")
# print(df["geolocation_zip_code_prefix"].duplicated().sum())

# print("\nSample records:")
# print(df.head())

# Cleaning geo location duplicates 
df = df.drop_duplicates()

# Aggregate coordinates by ZIP code 
df = df.groupby("geolocation_zip_code_prefix").agg({
    "geolocation_lat": "mean",
    "geolocation_lng": "mean",
    "geolocation_city": "first",
    "geolocation_state": "first"
}).reset_index()

# Save cleaned dataset
df.to_csv("data/processed/geolocation_clean.csv", index=False)

print("Original rows:", 1000163)
print("Cleaned rows:", len(df))
print("Geolocation cleaning completed!")


df = pd.read_csv("data/processed/geolocation_clean.csv")

print("Total rows:", len(df))
print("Duplicate ZIP codes:",
      df["geolocation_zip_code_prefix"].duplicated().sum())
print("Missing values:", df.isnull().sum().sum())
print(df.head())