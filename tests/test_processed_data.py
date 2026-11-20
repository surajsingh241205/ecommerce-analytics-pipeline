
from pathlib import Path
import pandas as pd

# Project root directory
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data" / "processed"

# Expected cleaned datasets
EXPECTED_FILES = [
    "olist_category_translation_cleaned_dataset.csv",
    "olist_customers_cleaned_dataset.csv",
    "olist_geolocation_cleaned_dataset.csv",
    "olist_order_items_cleaned_dataset.csv",
    "olist_order_payments_cleaned_dataset.csv",
    "olist_order_reviews_cleaned_dataset.csv",
    "olist_orders_cleaned_dataset.csv",
    "olist_products_cleaned_dataset.csv",
    "olist_sellers_cleaned_dataset.csv",
]


def test_processed_files_exist():
    """Check that all expected cleaned CSV files exist."""
    for filename in EXPECTED_FILES:
        assert (DATA_DIR / filename).is_file(), f"Missing file: {filename}"


def test_processed_files_are_not_empty():
    """Check that every cleaned CSV contains data."""
    for filename in EXPECTED_FILES:
        file_path = DATA_DIR / filename
        assert file_path.stat().st_size > 0, f"Empty file: {filename}"


def test_processed_data_has_no_duplicate_rows():
    """Check for exact duplicate rows in every cleaned CSV."""
    for filename in EXPECTED_FILES:
        df = pd.read_csv(DATA_DIR / filename)
        duplicates = df.duplicated().sum()

        assert duplicates == 0, (
            f"{filename} contains {duplicates} duplicate rows"
        )


def test_processed_data_has_columns():
    """Check that every cleaned CSV has at least one column."""
    for filename in EXPECTED_FILES:
        df = pd.read_csv(DATA_DIR / filename, nrows=1)
        assert len(df.columns) > 0, f"No columns found: {filename}"
