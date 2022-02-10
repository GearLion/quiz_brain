from requests import get
import json

PARAMS = {
    "amount": 10,
    "type": "boolean"
}

question_api = get("https://opentdb.com/api.php", params=PARAMS).text
response = json.loads(question_api)
question_data = response["results"]