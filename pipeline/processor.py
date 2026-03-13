def process_data(data):
    processed = []

    for item in data:
        processed.append({
            "id": item["id"],
            "title": item["title"],
            "completed": item["completed"]
        })

    return processed