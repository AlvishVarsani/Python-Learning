from copy import deepcopy
from pydoc import text

class Chunker:
    def __init__(self, chunk_size=500,overlap=100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_document(self, document):

     text = document.page_content
     chunks = []
     start = 0

     while start < len(text):

        end = start + self.chunk_size

        chunk_text = text[start:end]

        chunk = deepcopy(document)

        chunk.page_content = chunk_text

        chunk.metadata["chunk_start"] = start

        chunk.metadata["chunk_end"] = end

        chunks.append(chunk)

        start = end - self.overlap

        return chunks