from loader.pdf_loader import PDFLoader
from preprocessing.cleaner import TextCleaner
from pathlib import Path
from chunking.chunker import Chunker
from embedding.embedding_service import EmbeddingService

# Load the PDF document
BASE_DIR = Path(__file__).parent
loader = PDFLoader(BASE_DIR / "data" / "Leave_Policy.pdf")
documents = loader.load()


# Clean the text of each document
cleaner = TextCleaner()
for document in documents:
    document.page_content = cleaner.clean(document.page_content)


# Chunk the cleaned documents
chunker = Chunker(chunk_size=500, overlap=100)
all_chunks=[]
for document in documents:
    chunks = chunker.split_document(document)
    all_chunks.extend(chunks)
 

# Embed the chunks using the embedding service    
service = EmbeddingService()
for chunk in chunks:
    embedding = service.model.encode(chunk.page_content)
    
    
