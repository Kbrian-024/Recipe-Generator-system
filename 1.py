from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Define your recipes
recipes = [
    {
        "title": "Spaghetti Bolognese",
        "ingredients": [
            "400g spaghetti",
            "500g minced beef",
            "1 onion, chopped",
            "2 cloves garlic, minced",
            "1 can (400g) chopped tomatoes",
            "2 tablespoons tomato paste",
            "1 teaspoon dried oregano",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "Cook spaghetti according to package instructions until al dente. Drain and set aside.",
            "In a large skillet, brown minced beef over medium heat until cooked through. Add chopped onion and minced garlic, and cook until softened.",
            "Stir in chopped tomatoes, tomato paste, and dried oregano. Season with salt and pepper to taste. Simmer for 10-15 minutes.",
            "Serve the Bolognese sauce over cooked spaghetti. Optionally, garnish with grated Parmesan cheese and fresh basil leaves."
        ]
    },
    # Add more recipes here
]

# Custom Jinja2 filter for emulating enumerate function
@app.template_filter('enumerate')
def jinja2_enumerate(iterable):
    return enumerate(iterable)

@app.route('/')
def index():
    return render_template('1.html', recipes=recipes)

@app.route('/generate', methods=['POST'])
def generate():
    recipe_index = int(request.form['recipe_index'])
    selected_recipe = recipes[recipe_index]
    return render_template('recipe.html', recipe=selected_recipe)

if __name__ == '__main__':
    app.run(debug=True)
