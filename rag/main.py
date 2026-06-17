from loader.pdf_loader import PDFLoader
from perprocessing.cleaner import TextCleaner
from pathlib import Path
from chunking.chunker import Chunker
from chunking.recusive_chunking import RecursiveChunker
from embedding.embedding_service import EmbeddingService
from vectordb.faiss_service import FAISSService
from retriever.retriever import Retriever
from prompt.prompt_builder import PromptBuilder
from llm.groq_services import GroqService

# Load the PDF document
BASE_DIR = Path(__file__).parent
loader = PDFLoader(BASE_DIR / "data" / "Leave_Policy.pdf")
documents = loader.load()


# Clean the text of each document
cleaner = TextCleaner()
for document in documents:
    document.page_content = cleaner.clean(document.page_content)


# Chunk the cleaned documents

#This is not chunking based on semantic meaning, it is just splitting the text into fixed size chunks.
# chunker = Chunker(chunk_size=500, overlap=100)
# all_chunks=[]
# for document in documents:
#     chunks = chunker.split_document(document)
#     all_chunks.extend(chunks)

chunker = RecursiveChunker(
    chunk_size=500,
    chunk_overlap=50
)

all_chunks = chunker.split_documents(documents)
 

# Embedding the chunks using the embedding service   

#Here the chunks are done in for loop which takes time, but you can also do it in batch if you want to. 
embedding_service = EmbeddingService()
faiss_service = FAISSService()

text=[all_chunk.page_content for all_chunk in all_chunks]  
vectors=embedding_service.embed(text)

#Doing this in for loop to assign the embedding to the chunked document.
for doc, vector in zip(all_chunks, vectors):

    doc.embedding = vector  

faiss_service.add_documents(all_chunks)

#This is to save the index and documents, so that we can load it later without having to do all the processing again.
faiss_service.save_index(BASE_DIR / "data" / "vector.index")
faiss_service.save_documents(BASE_DIR / "data" / "documents.pkl")
    
retriever = Retriever(
    embedding_service=embedding_service,
    faiss_service=faiss_service,
    top_k=3
)
prompt_builder = PromptBuilder()

groq_service = GroqService()

while True:

    question = input(
        "\nAsk Question : "
    )

    if question.lower() == "exit":
        break

    documents = retriever.retrieve(question)

    prompt = prompt_builder.build(

        question,

        documents

    )

    answer = groq_service.generate(prompt)

    print("\nAnswer\n")

    print(answer)