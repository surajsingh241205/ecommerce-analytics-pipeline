import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        os.getenv("DATABASE_URL")
    )
    
    
if __name__ == "__main__":
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT version();")
        print("Database connected sucessfully !")
        print(cursor.fetchone()[0])
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Connection Failed : {e}")