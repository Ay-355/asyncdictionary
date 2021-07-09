class WordNotFound(Exception):
    """Error when the API can not find a word"""


class APIError(Exception):
    """Broad Exception raised when the API did not return a good response"""
    __slots__ = ("status_code", "error_message")

    def __init__(self, code: int, error_message: str):
        self.status_code = code
        self.error_message = error_message

    def __repr__(self) -> str:
        return f"<APIError status_code={self.status_code} message={self.error_message}>"

    def __str__(self) -> str:
        return self.error_message
