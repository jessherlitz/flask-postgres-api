from dotenv import load_dotenv
import os
import psycopg2


load_dotenv()


def get_db_connection():
    conn = psycopg2.connect(host=os.getenv('DB_HOST'),
                            database=os.getenv('DB_NAME'),
                            user=os.getenv('DATABASE_USER'),
                            password=os.getenv('DATABASE_PASS'))
    return conn
