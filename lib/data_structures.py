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
    }
]

def get_names():
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods():
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods():
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(cuisine):
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)

def print_spiciest_foods():
    spiciest_foods = get_spiciest_foods()
    for food in spiciest_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def average_heat_level():
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    return total_heat_level // num_foods
