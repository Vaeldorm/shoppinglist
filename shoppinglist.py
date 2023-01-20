# Main function will consist of a list of variables named as ingredients (i.e. chicken), as well as the print functions that the user will need at the end of their interaction to see all the items they will need to buy to make the meals they selected. The main function will also call on other functions to prompt the user and gather this aforementioned information. 
# def main():

# for loop to update ingredients
def update_count(selection):
    for dish in dishes:
        if dish == "Chicken":
            chicken_count += 1
        elif dish == "Ground Beef":
            ground_beef_count += 1

# get selection from user
def get_dish():
    print("Please choose a number:")
    for dish in dishes:
        print(dish["number"], dish["name"], sep=(" "))
    return int(input())
    
# main dict 
# "name":"dish", "ingredient1": "item", "ingredient2": "item", "ingredient3": "item", "ingredient4": "item", "ingredient4": "item"
dishes = [
    {"number": 1, "name": "Cajun Chicken Pasta", "ingredient1": "Chicken", "ingredient2": "Pasta", "ingredient3": "Red Bell Pepper", "ingredient4": "Green Bell Pepper", "ingredient4": "Cherry Tomatoes"},
    {"number": 2, "name":"Pesto Chicken Pasta", "ingredient1": "Chicken", "ingredient2": "Pasta", "ingredient3": "Basil", "ingredient4": "Pine Nuts", "ingredient4": "Cherry Tomatoes", "ingredient5": "Parmesan Cheese", "ingredient6": "Garlic"}
]

selection = get_dish()
chicken_count = 0
ground_beef_count = 0

# Test
# print(selection)


