
from src.transformation import transform_transaction

def test_tax_calculation():
    data = {
        "transaction_id": "T1001",
        "customer_id": "C101",
        "product": "Laptop",
        "quantity": 2,
        "unit_price": 50000,
        "state": "Telangana"
    }

    result = transform_transaction(data)

    assert result["subtotal"] == 100000
    assert result["tax_amount"] == 18000
    assert result["total_amount"] == 118000
    assert "processed_at" in result
