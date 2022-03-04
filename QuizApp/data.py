import requests
parameters = {
    "amount": "30",
    "type": "boolean",
    "category": "9"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
