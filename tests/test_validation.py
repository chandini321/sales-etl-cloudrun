
from src.validation import validate_transaction

def test_valid_transaction():
    data = {
        "transaction_id": "T1001",
        "customer_id": "C101",
        "product": "Laptop",
        "quantity": 2,
        "unit_price": 50000,
        "state": "Telangana"
    }

    is_valid, error = validate_transaction(data)

    assert is_valid is True
    assert error is None


def test_invalid_quantity():
    data = {
        "transaction_id": "T1001",
        "customer_id": "C101",
        "product": "Laptop",
        "quantity": 0,
        "unit_price": 50000,
        "state": "Telangana"
    }

    is_valid, error = validate_transaction(data)

    assert is_valid is False
    assert error is not None
