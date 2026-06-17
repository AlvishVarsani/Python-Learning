from pathlib import Path
from pypdf import PdfReader
from .document import Document

class PDFLoader:

    def __init__(self, pdf_path):
        self.pdf_path = Path(pdf_path)

    def load(self):

        reader = PdfReader(self.pdf_path)

        documents = []

        for page_number, page in enumerate(reader.pages):

            documents.append(
                Document(
                    page_content=page.extract_text(),
                    metadata={
                        "page": page_number + 1,
                        "source": self.pdf_path.name
                    }
                )
            )

        return documents