import pandas as pd 
from pathlib import Path 

DATA_DIR = Path("data/raw")

# Identify the missing values by rows

# for file in DATA_DIR.glob("*.csv"):
#     df = pd.read_csv(file)

#     print(f"\n--- {file.name} ---")
#     print("Total Rows:", len(df))
#     print("Duplicate Rows:", df.duplicated().sum())
#     print("Missing Values:", df.isnull().sum().sum())
    
# Identify the missing values by Columns
for file in DATA_DIR.glob("*.csv"):
    df = pd.read_csv(file)

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if not missing.empty:
        print(f"\n--- {file.name} ---")
        print(missing)



