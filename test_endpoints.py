from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)

def test_post_prob_enfermedad_cardiaca():
    with open('testsData/test_input.json') as file:
        data = json.load(file)
    
    response = client.post("/probEnfermedadCardiaca", json=data)
    assert response.status_code == 200, "Error con el servicio"
    assert type(response.json()['prob']) is float, "La probabilidad debe ser un numero decimal"
    assert response.json()['prob'] <= 1, "La probabilidad supera a 1"