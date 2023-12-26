from flask import Flask , render_template
import pandas as pd
import requests


app = Flask(__name__)


@app.route('/')
def intro():
    return """<h1> hello chef ! </h1>
        <a href="/login">click here to login</a>
"""


@app.route('/login')
def login():
    return """
    <form action="">
        <b><label for="">username: </label></b><br>
        <input type="text"><br><br>

        <b><label for="">password: </label></b><br>
        <input type="password"><br><br>

        <input type="submit">

    </form>"""

@app.route('/recipe')
def recipe():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    data = response.json()
    meal_data = data['meals'][0]

    return render_template('recipe.html', 
                           meal=meal_data['strMeal'], 
                           category=meal_data['strCategory'], 
                           area=meal_data['strArea'], 
                           instructions=meal_data['strInstructions'], 
                           image=meal_data['strMealThumb'], 
                           tags=meal_data['strTags'])




if __name__ == '__main__':
    app.run()