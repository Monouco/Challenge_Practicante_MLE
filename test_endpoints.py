from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)

def test_post_prob_enfermedad_cardiaca():
    with open('test_input.json') as file:
        data = json.load(file)
    
    response = client.post("/probEnfermedadCardiaca", json=data)
    assert response.status_code == 500