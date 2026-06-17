from dataclasses import dataclass

@dataclass
class Document:
    page_content: str
    metadata: dict
    embedding: Optional[np.ndarray]=None
