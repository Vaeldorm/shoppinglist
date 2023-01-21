def main():
    recipes = []
    while True:
        recipe_name = input("Please enter the name of the dish (or 'q' to quit). ")
        if recipe_name == 'q':
            break
        ingredients = input("Enter ingredients for the recipe, separated by commas: ").split(", ")
        recipes.append({recipe_name: ingredients})
    print("Recipes:")
    for recipe in recipes:
        for name, ingredient in recipe.items():
            print("{")
            print(f"\"{name}\": [")
            for ing in ingredient:
                print(f"\t\"{ing}\",")
            print("]")
            print("},")
main()