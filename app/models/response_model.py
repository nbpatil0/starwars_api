from typing import Any

class ApiResponse:
    def __init__(self, data: Any, status: str = 'success', message: str = None, pagination: dict = None, **kwargs) -> None:
        self.status = status
        self.message = message
        self.data = data
        if pagination:
            self.pagination = pagination
