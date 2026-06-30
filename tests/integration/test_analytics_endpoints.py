from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_top_categories_endpoint_with_test_data():
    response = client.get("/top-categories")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 3
    assert data[0]["product_category_name"] == "electronics"
    assert data[0]["revenue"] == 300.0


def test_monthly_revenue_endpoint_with_test_data():
    response = client.get("/monthly-revenue")

    assert response.status_code == 200

    data = response.json()

    assert data[0]["month"] == "2024-01"
    assert data[0]["revenue"] == 150.0


def test_orders_by_state_endpoint_with_test_data():
    response = client.get("/orders-by-state")

    assert response.status_code == 200

    data = response.json()

    assert data[0]["customer_state"] == "RJ"
    assert data[0]["orders"] == 2