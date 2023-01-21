def print_menu(dishes):
    for idx, dish in enumerate(dishes):
        print(f"{idx + 1}. {dish['name']}")

def get_ingredients_from_dish(selected_dish):
    name = selected_dish["name"]
    ingredients = [
        ingredient
        for ingredient in selected_dish.values()
        if ingredient != name
    ]
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
            "name": "Cajun Chicken Pasta",
            "ingredient1": "Chicken",
            "ingredient2": "Pasta",
            "ingredient3": "Red Bell Pepper",
            "ingredient4": "Green Bell Pepper",
            "ingredient5": "Cherry Tomatoes",
        },
        {
            "name": "Pesto Chicken Pasta",
            "ingredient1": "Chicken",
            "ingredient2": "Pasta",
            "ingredient3": "Basil",
            "ingredient4": "Pine Nuts",
            "ingredient4": "Cherry Tomatoes",
            "ingredient5": "Parmesan Cheese",
            "ingredient6": "Garlic",
        },
    ]
    print_menu(dishes)

    while True:
        choice = input("Please type the number for the meal you would like to cook (or 'q' to quit). ")
        if choice == "q":
            break
        try:
            choice = int(choice)
            selected_dish = dishes[choice - 1]
            ingredients = get_ingredients_from_dish(selected_dish)
            for ingredient in ingredients:
                shopping_list = add_ingredients_to_shopping_list(ingredient, shopping_list)
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number or 'q' to quit. ")

    print(shopping_list)


main()
