import psycopg
from decouple import config

DATABASE_URL = config("DATABASE_URL")

try:
    with psycopg.connect(DATABASE_URL, sslmode='require') as conn:
        print("Successfully connected to the database!")
except Exception as e:
    print(f"Error connecting to the database: {e}")