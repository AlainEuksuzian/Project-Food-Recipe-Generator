from flask import Flask , render_template, flash, redirect
from forms import Login, Signup
import pandas as pd
import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = 'My_food_recipe_app'



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.jinja')

@app.route('/login', methods=['POST','GET'])
def login():
    form = Login()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        flash('the username is: {u}'.format(u=username))
        flash('the password is {p}'.format(p=password))
        return redirect('formTester')
    return render_template('login.jinja', form=form)


@app.route('/formTester')
def form_test():
    return render_template('formTester.jinja')



@app.route('/signup')
def sign_up():
    return render_template('signup.jinja')

@app.route('/recipe')
def recipe():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    data = response.json()
    meal_data = data['meals'][0]

    return render_template('recipe.jinja', 
                           meal=meal_data['strMeal'], 
                           category=meal_data['strCategory'], 
                           area=meal_data['strArea'], 
                           instructions=meal_data['strInstructions'], 
                           image=meal_data['strMealThumb'], 
                           tags=meal_data['strTags'])




if __name__ == '__main__':
    app.run(debug=True)