class ResumeAnalyzerError(Exception):
    """Base exception for Resume Analyzer application."""
    pass

class LLMAPIError(ResumeAnalyzerError):
    """Raised when there is an issue with the LLM API request (e.g., 4xx, 5xx)."""
    pass

class RateLimitError(LLMAPIError):
    """Raised specifically when rate limits are exceeded (HTTP 429)."""
    pass

class NetworkError(LLMAPIError):
    """Raised when there is a network connectivity issue."""
    pass

class PDFExtractionError(ResumeAnalyzerError):
    """Raised when there is an error extracting text from the PDF file."""
    pass
