from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_summary_endpoint_with_test_data():
    response = client.get("/summary")

    assert response.status_code == 200

    data = response.json()

    assert data["total_revenue"] == 575.0
    assert data["total_orders"] == 5
    assert data["average_order_value"] == 115.0