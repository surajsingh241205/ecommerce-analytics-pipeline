
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

EXPECTED_TABLES = [
    "customers",
    "geolocation",
    "orders",
    "order_items",
    "order_payments",
    "order_reviews",
    "products",
    "sellers",
    "category_translation",
]


def get_database_engine():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("DATABASE_URL is missing")

    if database_url.startswith("postgresql://"):
        database_url = database_url.replace(
            "postgresql://",
            "postgresql+psycopg2://",
            1
        )

    return create_engine(database_url)


def test_staging_tables_exist_and_have_data():
    engine = get_database_engine()

    try:
        with engine.connect() as connection:
            for table in EXPECTED_TABLES:
                result = connection.execute(
                    text("""
                        SELECT COUNT(*)
                        FROM staging.tables
                        WHERE table_name = :table_name
                    """.replace("staging.tables", "information_schema.tables")),
                    {"table_name": table}
                )

                assert result.scalar() == 1, (
                    f"Missing staging table: {table}"
                )

                count = connection.execute(
                    text(f'SELECT COUNT(*) FROM staging."{table}"')
                ).scalar()

                assert count > 0, (
                    f"Staging table is empty: {table}"
                )
    finally:
        engine.dispose()
