from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_users():
    response = client.post("/users/", json={"name": "Leo", "city": "Moscow"})
    assert response.status_code == 200
    assert response.text == '"Успешно, проверь запись в базе данных"'


def test_places():
    response = client.get("/places/", params={'place':'shop', 'city':'Moscow'})
    assert response.status_code == 200
    assert response.text == '"Успешно, проверь запись в базе данных"'