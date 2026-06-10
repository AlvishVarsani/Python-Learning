from pathlib import Path
import csv
from pypdf import PdfReader

BASE_DIR = Path(__file__).parent

print("BASE_DIR:", BASE_DIR)

csv_file = BASE_DIR / "users.csv"
if csv_file.exists():
    print("CSV file exists at:", csv_file)
else:    print("CSV file does not exist at:", csv_file)

reports = BASE_DIR / "reports"

reports.mkdir(exist_ok=True)

#To find all .csv/.pdf we have in the BASE_DIR.glob
csv_files = list(BASE_DIR.glob("*.csv"))
pdf_files = list(BASE_DIR.glob("*.pdf"))

with open(csv_file, newline="") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
        

with open(csv_file) as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row["name"]) 

#Writing to a new CSV file
new_csv_file = BASE_DIR / "new_users.csv"
with open(new_csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "email"])
    writer.writerow(["Alice", 30, "alice@example.com"])


##PDF reader
file=PdfReader(BASE_DIR / "sample.pdf")
print("Number of pages:", len(file.pages))
for page in file.pages:
    print(page.extract_text())