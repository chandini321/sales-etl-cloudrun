
from datetime import datetime, timezone
from decimal import Decimal

def transform_transaction(data):

    quantity = Decimal(str(data["quantity"]))
    unit_price = Decimal(str(data["unit_price"]))

    subtotal = quantity * unit_price
    tax_rate = Decimal("0.18")
    tax_amount = subtotal * tax_rate
    total_amount = subtotal + tax_amount

    return {
        **data,
        "subtotal": float(subtotal),
        "tax_rate": float(tax_rate),
        "tax_amount": float(tax_amount),
        "total_amount": float(total_amount),
        "processed_at": datetime.now(
            timezone.utc
        ).isoformat()
    }
