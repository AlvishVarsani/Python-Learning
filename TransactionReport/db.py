import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, FETCH_TRANSACTIONS_QUERY

def get_db_connection():
    """
    Establish and return a connection to the local MySQL database.
    Uses credentials loaded from the .env file.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def fetch_transactions(connection, merchant_id, year):
    """
    Fetch transactions for a given merchant and year from the database.
    """
    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(FETCH_TRANSACTIONS_QUERY, (merchant_id, year))
        records = cursor.fetchall()
        return records
    except Error as e:
        print(f"Error executing query: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
