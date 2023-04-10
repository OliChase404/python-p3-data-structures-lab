spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# def get_names(spicy_foods):
#     response = []
#     for i in spicy_foods: response.append(i['name'])
#     return response


def get_names(spicy_foods):
    return [i["name"] for i in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [i for i in spicy_foods if i['heat_level'] > 5]


def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        print(f"{i['name']} ({i['cuisine']}) | Heat Level: {'🌶' * i['heat_level']}")


# print_spicy_foods(spicy_foods)


# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     return [i for i in spicy_foods if i['cuisine'] == cuisine]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None


# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     resp = [i for i in spicy_foods if i['cuisine'] == cuisine]
#     return resp

# resp = get_spicy_food_by_cuisine(spicy_foods, 'Thai')

# print(resp)


def print_spiciest_foods(spicy_foods):
    spicy = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy)


# def get_average_heat_level(spicy_foods):
#     average_heat_level = 0
#     for i in spicy_foods:
#         average_heat_level += i['heat_level']
#     average_heat_level /= len(spicy_foods)
#     return average_heat_level

def get_average_heat_level(spicy_foods):
    return sum(i['heat_level'] for i in spicy_foods) / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
