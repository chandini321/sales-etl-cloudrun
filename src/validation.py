
import json
from jsonschema import validate, ValidationError

def validate_transaction(data):

    with open("schemas/sales_schema.json") as file:
        schema = json.load(file)

    try:
        validate(instance=data, schema=schema)
        return True, None

    except ValidationError as error:
        return False, error.message
