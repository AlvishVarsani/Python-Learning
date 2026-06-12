import sys
import os

# Ensure the parent directory is in the path so we can import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import extract_text_from_pdf
from analyzer import analyze_resume_stream
from experiments import run_max_tokens_experiment, run_temperature_experiment
from exceptions import ResumeAnalyzerError

def main():
    print("=== Resume Analyzer AI ===")
    
# 1. Ask the user for the PDF file path
    pdf_path = input("Please paste the absolute path to the resume PDF file: ").strip()
    
    if not os.path.isfile(pdf_path):
        print(f"Error: The file '{pdf_path}' does not exist.")
        sys.exit(1)

    print(f"\nExtracting text from {pdf_path}...")
    try:
        resume_text = extract_text_from_pdf(pdf_path)
    except ResumeAnalyzerError as e:
        print(f"Error extracting text: {e}")
        sys.exit(1)
        
    print(f"Successfully extracted {len(resume_text)} characters.\n")
    
    while True:
        print("Select an option:")
        print("1. Standard Resume Analysis")
        print("2. Run Max Tokens Experiment (100 vs 1000)")
        print("3. Run Temperature Experiment (0.1 vs 1.0)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\nStarting standard analysis (streaming)...\n" + "-"*40)
            try:
                for chunk in analyze_resume_stream(resume_text):
                    print(chunk, end="", flush=True)
                print("\n" + "-"*40 + "\n")
            except ResumeAnalyzerError as e:
                print(f"\nAnalysis failed: {e}\n")
                
        elif choice == '2':
            run_max_tokens_experiment(resume_text)
            
        elif choice == '3':
            run_temperature_experiment(resume_text)
            
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting.")
        sys.exit(0)
