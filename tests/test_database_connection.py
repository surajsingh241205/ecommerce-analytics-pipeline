
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


# Load local .env when running tests on your computer.
# GitHub Actions will use its DATABASE_URL environment variable.
ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")


def test_neon_database_connection():
    """Verify that Neon PostgreSQL is accessible."""

    database_url = os.getenv("DATABASE_URL")

    assert database_url, "DATABASE_URL environment variable is missing"

    # Use the psycopg2 driver.
    if database_url.startswith("postgresql://"):
        database_url = database_url.replace(
            "postgresql://",
            "postgresql+psycopg2://",
            1
        )

    engine = create_engine(database_url)

    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.scalar() == 1
    finally:
        engine.dispose()
