from google.cloud import bigquery

def load_transaction(data):
    client = bigquery.Client()

    table_id = (
        "pioneering-flow-436606-t9.sales_dataset.sales_transactions"
    )

    errors = client.insert_rows_json(
        table_id,
        [data]
    )

    if errors:
        raise Exception(f"BigQuery insert failed: {errors}")

    return True