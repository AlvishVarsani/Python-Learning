from db import get_db_connection, fetch_transactions
from report import generate_csv, generate_pdf_report

def main():
    # Prompt the user interactively
    try:
        merchant_id = int(input("Enter Merchant ID: "))
    except ValueError:
        print("Invalid Merchant ID. Must be an integer.")
        return

    try:
        year = int(input("Enter Year (e.g., 2023): "))
    except ValueError:
        print("Invalid Year. Must be an integer.")
        return

    print(f"\nProcessing report for Merchant ID: {merchant_id}, Year: {year}")
    
    # Establish DB Connection (reads from .env automatically)
    connection = get_db_connection()
    if not connection:
        return

    try:
        print("Fetching transactions from database...")
        records = fetch_transactions(connection, merchant_id, year)
        
        if not records:
            print(f"No transactions found for Merchant ID {merchant_id} in year {year}.")
            return
            
        print(f"Found {len(records)} transactions.")

        csv_filename = f"merchant_{merchant_id}_transactions_{year}.csv"
        pdf_filename = f"merchant_{merchant_id}_summary_{year}.pdf"

        # Generate Reports
        generate_csv(records, csv_filename)
        generate_pdf_report(records, merchant_id, year, pdf_filename)
        
        print("\nProcess completed successfully.")
        
    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()
