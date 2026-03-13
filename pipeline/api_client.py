import requests

def fetch_data(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API request failed")

    return response.json()