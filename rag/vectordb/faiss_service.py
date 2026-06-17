import faiss
import pickle
import numpy as np
from typing import List
from pathlib import Path
from loader.document import Document

BASE_DIR = Path(__file__).parent
class FAISSService:

    def __init__(self, dimension: int = 384):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.documents: List[Document] = []


    def add_documents(self, documents: List[Document]) -> None:

        if not documents:
            raise ValueError("Document list is empty.")

        embeddings = []

        for document in documents:

            if len(document.embedding) != self.dimension:
                raise ValueError(
                    f"Expected embedding dimension "
                    f"{self.dimension}, "
                    f"got {len(document.embedding)}"
                )

            embeddings.append(document.embedding)

        embeddings = np.asarray(
            embeddings,
            dtype=np.float32
        )

        self.index.add(embeddings)
        self.documents.extend(documents)


    def search(self,query_embedding: np.ndarray,top_k: int = 5):
        if len(query_embedding) != self.dimension:
            raise ValueError(
                f"Expected query dimension "
                f"{self.dimension}, "
                f"got {len(query_embedding)}"
            )

        query_embedding = np.asarray([query_embedding],dtype=np.float32)

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0]
        ):

            if index == -1:
                continue

            results.append({
                "document": self.documents[index],
                "distance": float(distance)
            })

        return results


    def save_index(
        self,
        file_path
    ):

        faiss.write_index(
            self.index,
            str(file_path)
        )

    def load_index(
        self,
        file_path
    ):

        self.index = faiss.read_index(
            str(file_path)
        )


    def save_documents(
        self,
        file_path
    ):
    
        with open(str(file_path), "wb") as file:
            pickle.dump(
                self.documents,
                file
            )


    def load_documents(
        self,
        file_path: str = "data/documents.pkl"
    ):

        with open(file_path, "rb") as file:
            self.documents = pickle.load(file)


    @property
    def total_documents(self):
        return len(self.documents)