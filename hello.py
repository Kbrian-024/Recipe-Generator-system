# Load recipes from recipes.txt
def load_recipes():
    with open('recipes.txt', 'r') as file:
        recipes = file.read().split('\n\n')  # Split recipes by empty lines
        print(recipes)
    return recipes




load_recipes()