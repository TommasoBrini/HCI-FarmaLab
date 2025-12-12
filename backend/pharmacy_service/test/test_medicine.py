from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_medicine():
    payload = {
        "name": "Tachipirina",
        "active_principle": "Paracetamolo",
        "producer": "Angelini",
        "side_effect": ["nausea", "vomito"]
    }
    r = client.post("/medicines", json=payload)
    assert r.status_code == 201
    med = r.json()
    assert med["name"] == "Tachipirina"
    assert med["side_effect"] == ["nausea", "vomito"]

    r2 = client.get(f"/medicines/{med['id']}")
    assert r2.status_code == 200
    assert r2.json()["active_principle"] == "Paracetamolo"
