from typing import Any
import requests


class ApiClient:
    """Small reusable API client for authorized test environments."""

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        return requests.get(
            f"{self.base_url}/{path.lstrip('/')}", timeout=self.timeout, **kwargs
        )

    def post(self, path: str, **kwargs: Any) -> requests.Response:
        return requests.post(
            f"{self.base_url}/{path.lstrip('/')}", timeout=self.timeout, **kwargs
        )
