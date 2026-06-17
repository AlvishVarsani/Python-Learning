from dataclasses import dataclass
from typing import Optional
import numpy as np

@dataclass
class Document:
    page_content: str
    metadata: dict
    embedding: Optional[np.ndarray]=None
