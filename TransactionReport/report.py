import csv
from fpdf import FPDF
from datetime import datetime
from config import SUCCESS_STATE_STRING

def generate_csv(records, output_filename):
    """
    Generate a CSV file from the fetched records using the standard csv library.
    """
    if not records:
        print("No records found to write to CSV.")
        return

    fieldnames = ['date', 'transactionId', 'merchantName', 'amount', 'txState', 'txType']
    
    try:
        with open(output_filename,'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in records:
                # Format date as string if it's a date object
                row_dict = row.copy()
                if row_dict['date']:
                    row_dict['date'] = str(row_dict['date'])
                writer.writerow(row_dict)
        print(f"Successfully generated CSV file: {output_filename}")
    except Exception as e:
        print(f"Error generating CSV: {e}")

def generate_pdf_report(records, merchant_id, year, output_filename):
    """
    Calculate summary statistics and generate a PDF report.
    """
    success_amount = 0.0
    non_success_amount = 0.0
    success_count = 0
    failure_count = 0

    # Calculate metrics
    for row in records:
        amount = float(row['amount']) if row['amount'] is not None else 0.0
        state = str(row['txState']).upper() if row['txState'] else ""

        if state == SUCCESS_STATE_STRING:
            success_amount += amount
            success_count += 1
        else:
            non_success_amount += amount
            failure_count += 1

    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(200, 10, txt="Transaction Summary Report", ln=True, align='C')
    pdf.ln(10)

    # Details
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Merchant ID: {merchant_id}", ln=True)
    pdf.cell(200, 10, txt=f"Year: {year}", ln=True)
    pdf.cell(200, 10, txt=f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(10)

    # Summary Data
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Transaction Metrics:", ln=True)
    pdf.set_font("Arial", size=12)
    
    # Use formatted strings for currency
    pdf.cell(200, 10, txt=f"Total Success Amount: ${success_amount:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Total Non-Success Amount: ${non_success_amount:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Total Success Count: {success_count}", ln=True)
    pdf.cell(200, 10, txt=f"Total Failure Count: {failure_count}", ln=True)

    try:
        pdf.output(output_filename)
        print(f"Successfully generated PDF report: {output_filename}")
    except Exception as e:
        print(f"Error generating PDF: {e}")
