def print_menu(dishes):
    for idx, dish in enumerate(dishes):
        print(f"{idx + 1}. {list(dish.keys())[0]}")


def get_ingredients_from_dish(selected_dish):
    ingredients = [ingredient for ingredient in selected_dish]
    return ingredients


def add_ingredients_to_shopping_list(ingredient, shopping_list):
    if ingredient in shopping_list:
        shopping_list[ingredient] += 1
    else:
        shopping_list[ingredient] = 1
    return shopping_list


def main():
    shopping_list = {}
    dishes = [
        {
            "Cajun Chicken Pasta": [
                "Chicken",
                "Pasta",
                "Red Bell Pepper",
                "Green Bell Pepper",
                "Cherry Tomatoes",
            ]
        },
        {
            "Pesto Chicken Pasta": [
                "Chicken",
                "Pasta",
                "Basil",
                "Pine Nuts",
                "Cherry Tomatoes",
                "Parmesan Cheese",
                "Garlic",
            ]
        },
                {
            "Spinach and Feta Omelette": [
                "Eggs",
                "Spinach",
                "Sour Cream",
            ]
        },
        {
            "Migas": [
                "Eggs",
                "Beans (Refried)",
                "Corn Tortillas",
            ]
        },
        {
            "Ranchero Plate": [
                "Eggs",
                "Beans (Refried)",
                "Potatoes",
            ]
        },
        {
            "Taco Soup": [
                "Pinto Beans",
                "Rotel",
                "Ground Beef",
                "Hidden Valley Ranch Seasoning",
                "Taco Seasoning",
                "Corn",
                "Diced Green Chiles",
            ]
        },
        {
            "Chicekn Spaghetti": [
                "Chicken",
                "Pasta",
                "Chicken Broth",
                "Velveeta",
                "Chicken and Mushroom Soup",
                "Chicken and Celery Soup",
                "Celery",
                "Green Bell Pepper",
                "Onion",
            ]
        },
    ]
    print_menu(dishes)

    while True:
        choice = input("Please type the number for the meal you would like to cook (or 'q' to quit). ")
        if choice == "q":
            break

        try:
            choice = int(choice)
            selected_dish = list(dishes[choice - 1].values())[0]
            ingredients = get_ingredients_from_dish(selected_dish)
            for ingredient in ingredients:
                shopping_list = add_ingredients_to_shopping_list(ingredient, shopping_list)
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number or 'q' to quit.")

    print()
    print("Shopping list:")
    for item, value in sorted(shopping_list.items()):
        print(f"{item}: {value}")


main()
