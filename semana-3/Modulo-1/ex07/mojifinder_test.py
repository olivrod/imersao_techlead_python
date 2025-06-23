from fastapi.testclient import TestClient
from unicodedata import name as unicode_name

from mojifinder import app

client = TestClient(app)


def test_root_endpoint() -> None:
    """Test the root endpoint returns the HTML form."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"

    # Check presence of input field named "q"
    content = response.content.decode()
    assert '<input name="q"' in content

    # Verify it matches the form content from app.state.form
    assert content == app.state.form


def test_search_endpoint() -> None:
    """Test the /search endpoint returns correct characters and names."""
    # Search for heart emoji characters
    response = client.get("/search?q=heart")

    assert response.status_code == 200
    data = response.json()

    # Verify we got results
    assert len(data) > 0

    # Check that returned data has the expected structure
    for item in data:
        assert "code" in item
        assert "char" in item
        assert "name" in item
        assert "HEART" in item["name"]

        # Verify the name matches what unicodedata would return
        assert item["name"] == unicode_name(item["char"])
