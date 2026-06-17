from typing import List

from loader.document import Document


class PromptBuilder:

    def build(
        self,
        question: str,
        documents: List[Document]
    ) -> str:

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        prompt = f"""
You are an AI assistant.

Answer ONLY using the provided context.

If the answer is not available in the context,
say:

"I don't have enough information to answer that."

Context:
-------------------------
{context}
-------------------------

Question:
{question}

Answer:
"""

        return prompt.strip()