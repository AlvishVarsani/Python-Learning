from typing import List

from loader.document import Document
from embedding.embedding_service import EmbeddingService
from vectordb.faiss_service import FAISSService


class Retriever:

    def __init__(
        self,
        embedding_service: EmbeddingService,
        faiss_service: FAISSService,
        top_k: int = 5,
        max_distance: float = None
    ):

        self.embedding_service = embedding_service
        self.faiss_service = faiss_service
        self.top_k = top_k
        self.max_distance = max_distance

    def retrieve(self, question: str) -> List[Document]:

        # Generate embedding for user query
        query_embedding = self.embedding_service.embed(question)

        # Search FAISS
        results = self.faiss_service.search(
            query_embedding=query_embedding,
            top_k=self.top_k
        )

        documents = []

        for result in results:

            distance = result["distance"]

            # Optional filtering
            if self.max_distance is not None:
                if distance > self.max_distance:
                    continue

            document = result["document"]

            documents.append(document)

        return documents