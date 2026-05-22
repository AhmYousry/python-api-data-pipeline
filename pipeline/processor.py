def process_data(data):
    processed = []

    for item in data["products"]:
        processed.append({
            "id": item["id"],
            "title": item["title"],
            "category": item["category"],
            "price": item["price"],
            "rating": item["rating"]
        })

    return processed