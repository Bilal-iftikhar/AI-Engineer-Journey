import psycopg

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "employee_management",
    "user": "postgres",
    "password": "12345678"
}

def get_connection():
    connection = psycopg.connect(**DB_CONFIG)
    return connection