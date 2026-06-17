from copy import deepcopy
from typing import List


class RecursiveChunker:

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 50,
        separators=None
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.separators = separators or [
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]

    def split_documents(self, documents):

        all_chunks = []

        for document in documents:

            chunks = self._split_text(
                document.page_content,
                self.separators
            )

            for chunk in chunks:

                new_doc = deepcopy(document)

                new_doc.page_content = chunk

                all_chunks.append(new_doc)

        return all_chunks

    def _split_text(
        self,
        text: str,
        separators: List[str]
    ):

        if len(text) <= self.chunk_size:
            return [text.strip()]

        if not separators:
            return self._fixed_split(text)

        separator = separators[0]

        if separator == "":
            return self._fixed_split(text)

        pieces = text.split(separator)

        chunks = []
        current = ""

        for piece in pieces:

            candidate = (
                current + separator + piece
                if current
                else piece
            )

            if len(candidate) <= self.chunk_size:

                current = candidate

            else:

                if current:

                    chunks.extend(
                        self._split_text(
                            current,
                            separators[1:]
                        )
                    )

                current = piece

        if current:

            chunks.extend(
                self._split_text(
                    current,
                    separators[1:]
                )
            )

        return chunks

    def _fixed_split(self, text):

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(
                text[start:end]
            )

            start = end - self.chunk_overlap

        return chunks