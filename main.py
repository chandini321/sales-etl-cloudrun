import functions_framework
from flask import jsonify

from src.validation import validate_transaction
from src.transformation import transform_transaction
from src.bigquery_loader import load_transaction


@functions_framework.http
def order_event(request):

    if request.method != "POST":
        return jsonify({"error": "Only POST requests are allowed"}), 405

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    is_valid, error = validate_transaction(data)

    if not is_valid:
        return jsonify({"error": error}), 400

    transformed_data = transform_transaction(data)

    try:
        load_transaction(transformed_data)

        return jsonify({
            "message": "Transaction processed and loaded into BigQuery",
            "transaction": transformed_data
        }), 200

    except Exception as error:
        return jsonify({
            "error": "BigQuery loading failed",
            "details": str(error)
        }), 500