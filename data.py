import requests
from json import loads

url = "https://opentdb.com/api.php?amount=10&category=23&difficulty=easy&type=boolean"

string_data = requests.request("GET", url).text
dictionary_data = loads(string_data)
question_data = dictionary_data["results"]
