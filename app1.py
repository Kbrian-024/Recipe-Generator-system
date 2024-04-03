from flask import Flask, request, jsonify, render_template
import gpt_2_simple as gpt2
import os

app = Flask(__name__)

# Load recipes from recipes.txt
def load_recipes():
    with open('recipes.txt', 'r') as file:
        recipes = file.read().split('\n\n')  # Split recipes by empty lines
    return recipes

recipes = load_recipes()

# Define model parameters
model_name = "124M"
model_dir = os.path.join("models", model_name)
correct_model_dir = os.path.join("models", model_name)

# Check if the model directory exists
if not os.path.exists(model_dir):
    raise FileNotFoundError(f"Model directory {model_dir} does not exist.")

# Check if hparams.json exists
hparams_path = os.path.join(correct_model_dir, 'hparams.json')
if not os.path.exists(hparams_path):
    raise FileNotFoundError("hparams.json not found.")

# Load the GPT-2 model
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name=model_name, model_dir=model_dir)

@app.route('/')
def home():
    return render_template('main.html', recipes=recipes)

@app.route('/search_recipe', methods=['POST'])
def search_recipe():
    selected_index = int(request.form.get('recipe_name'))
    if 0 <= selected_index < len(recipes):
        selected_recipe = recipes[selected_index]
        generated_recipe = generate_recipe(selected_recipe)
        return jsonify({'recipe': generated_recipe})
    else:
        return jsonify({'error': 'Invalid recipe index'})

def generate_recipe(prompt):
    # Generate recipe using GPT-2
    try:
        generated_text = gpt2.generate(sess, prefix=prompt, return_as_list=True)[0]
        return generated_text
    except Exception as e:
        return f"Error generating recipe: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
