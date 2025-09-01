import pytest
from fastapi.testclient import TestClient


@pytest.fixture(name="client")
def _client():
    client = TestClient(app)
    yield client


def test_hello(client):
    """
    Root URL greets the wolrd.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
