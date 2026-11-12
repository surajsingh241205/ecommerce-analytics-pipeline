import pandas as pd 
from pathlib import Path 

DATA_DIR = Path("data/raw")

for file in DATA_DIR.glob("*csv"):
    df = pd.read_csv(file)
    
    print(f"\nFile : {file.name}")
    print(f"\n \n Rows : {df.shape[0]}")
    print(f"\n \n Columns : {df.shape[1]}")
    print(df.head(3))