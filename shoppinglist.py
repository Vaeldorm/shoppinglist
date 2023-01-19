# Main function will consist of a list of variables named as ingredients (i.e. chicken), as well as the print functions that the user will need at the end of their interaction to see all the items they will need to buy to make the meals they selected. The main function will also call on other functions to prompt the user and gather this aforementioned information. 
# def main():

# for loop to update ingredients
def update_list(dish):
    for item in dish:
        if item == "chicken":
            chicken_count += 1
        elif item == "ground_beef":
            ground_beef_count += 1

chicken_count = 0