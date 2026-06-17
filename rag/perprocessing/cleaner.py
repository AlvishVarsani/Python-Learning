import re

class TextCleaner:

    def clean(self, text: str) -> str:

        if not text:
            return ""

        # Remove invisible unicode characters
        text = text.replace("\u200b", "")
        text = text.replace("\u00a0", " ")

        # Remove page numbers
        text = re.sub(r"Page\s+\d+", "", text)

        # Remove repeated footers
        text = text.replace("Confidential", "")

        # Remove empty lines
        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        text = "\n".join(lines)

        # Normalize whitespace
        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()