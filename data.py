import requests
from json import loads


def set_category():
    categories_api = "https://opentdb.com/api_category.php"
    categories_data = requests.request("GET", categories_api).text
    categories_dict = loads(categories_data)
    num_categories = len(categories_dict["trivia_categories"])
    for n in range(0, num_categories):
        print(f"{n + 1}: {categories_dict['trivia_categories'][n]['name']}")
    category = input("Please type the number of the category you wish to answer.\n")

    good_input = False
    while not good_input:
        try:
            category = int(category)
        except ValueError:
            category = input("I'm sorry, but that didn't seem to be a valid category number. "
                             "Please type the number of the category you wish to answer\n")
        else:
            good_input = True

    cat = category + 8
    return cat


def set_difficulty():
    difficulty = input("Now, how hard should the questions be? Easy, Medium, or Hard?\n").lower()
    if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
        good_input = True
    else:
        good_input = False
    while not good_input:
        difficulty = input("I'm sorry. I didn't understand that answer. "
                           "How hard should the questions be? Easy, Medium, or Hard?\n").lower()
        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
            good_input = True
        else:
            good_input = False
    return difficulty


def question_cooker(cat, difficulty):
    question_api = f"https://opentdb.com/api.php?amount=10&category={cat}&difficulty={difficulty}&type=boolean"

    string_data = requests.request("GET", question_api).text
    question_data = loads(string_data)
    return question_data["results"]
