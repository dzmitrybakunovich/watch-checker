import main
from fastapi.testclient import TestClient

client = TestClient(main.app)


def test_pulse_check():
    response = client.get('/watch/pulse-check')
    assert response.status_code == 200
    assert response.json()['pulse'] is not None
