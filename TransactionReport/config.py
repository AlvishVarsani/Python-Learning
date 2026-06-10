import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configurations
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "pluto")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Business Logic Configuration
SUCCESS_STATE_STRING = "SUCCESS"

# SQL Queries
FETCH_TRANSACTIONS_QUERY = """
    SELECT 
        DATE(t.dateCreated) as date,
        t.transactionId,
        m.merchantName,
        t.amount,
        t.txState,
        t.txType
    FROM transaction t
    JOIN merchant m ON t.merchantId = m.merchantId
    WHERE t.merchantId = %s AND YEAR(t.dateCreated) = %s
"""
