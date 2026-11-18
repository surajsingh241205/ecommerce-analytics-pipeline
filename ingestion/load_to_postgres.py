
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Project paths
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data" / "processed"

# Database connection
load_dotenv(ROOT_DIR / ".env")
DATABASE_URL = os.getenv("DATABASE_URL")

DATABASE_URL = DATABASE_URL.replace(
    "postgresql://",
    "postgresql+psycopg2://",
    1
)

engine = create_engine(DATABASE_URL)

# Dataset filename → PostgreSQL table name
datasets = {
    "olist_customers_cleaned_dataset.csv": "customers",
    "olist_geolocation_cleaned_dataset.csv": "geolocation",
    "olist_orders_cleaned_dataset.csv": "orders",
    "olist_order_items_cleaned_dataset.csv": "order_items",
    "olist_order_payments_cleaned_dataset.csv": "order_payments",
    "olist_order_reviews_cleaned_dataset.csv": "order_reviews",
    "olist_products_cleaned_dataset.csv": "products",
    "olist_sellers_cleaned_dataset.csv": "sellers",
    "olist_category_translation_cleaned_dataset.csv": "category_translation"
}

def load_dataset(filename, table_name):
    file_path = DATA_DIR / filename

    df = pd.read_csv(file_path)

    df.to_sql(
        name=table_name,
        con=engine,
        schema="staging",
        if_exists="replace",
        index=False,
        chunksize=5000
    )

    print(f"{table_name}: {len(df)} rows loaded")


if __name__ == "__main__":
    with engine.connect() as connection:
        print("Database connected successfully!")

    for filename, table_name in datasets.items():
        load_dataset(filename, table_name)

    print("\nAll datasets loaded successfully!")
