from pipeline.api_client import fetch_data
from pipeline.processor import process_data
from pipeline.exporter import export_to_csv

API_URL = "https://jsonplaceholder.typicode.com/todos"

data = fetch_data(API_URL)

processed_data = process_data(data)

export_to_csv(processed_data, "data/output.csv")

print("Pipeline completed successfully")