from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "E-Commerce Analytics API"

def test_docs_available():
    response = client.get("/docs")

    assert response.status_code == 200

def test_summary_endpoint():
    response = client.get("/summary")

    assert response.status_code == 200

    data = response.json()

    assert "total_revenue" in data
    assert "total_orders" in data
    assert "average_order_value" in data

def test_top_categories_endpoint():
    response = client.get("/top-categories")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert "product_category_name" in data[0]
    assert "revenue" in data[0]


def test_monthly_revenue_endpoint():
    response = client.get("/monthly-revenue")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert "month" in data[0]
    assert "revenue" in data[0]


def test_orders_by_state_endpoint():
    response = client.get("/orders-by-state")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert "customer_state" in data[0]
    assert "orders" in data[0]