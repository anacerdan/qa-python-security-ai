from src.api_client import ApiClient


client = ApiClient("https://httpbin.org")


def test_get_status():
    response = client.get("/status/200")
    assert response.status_code == 200


def test_headers_endpoint_returns_json():
    response = client.get("/headers")
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")


def test_not_found_contract():
    response = client.get("/status/404")
    assert response.status_code == 404
