import os
from pypdf import PdfReader
from exceptions import PDFExtractionError

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from a given PDF file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        
        if not text.strip():
            raise PDFExtractionError("No text could be extracted from the PDF. It might be an image-based PDF.")
            
        return text
    except Exception as e:
        raise PDFExtractionError(f"Failed to extract text from PDF: {str(e)}")
