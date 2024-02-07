from flask import Flask , render_template, flash, redirect, url_for
from flask_migrate import Migrate
from forms import Login, Signup
import pandas as pd
import requests
from models import db, Users, Meal
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Alain E/Desktop/helloWorld/database.db'
app.config['SECRET_KEY'] = 'My_food_recipe_app'

db.init_app(app)
migrate = Migrate(app,db)



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



@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = Signup()
    if form.validate_on_submit():
        f_name = form.first_name.data
        l_name = form.last_name.data
        email = form.email.data
        uname = form.username.data
        password = form.password.data
        gender = form.gender.data

        try:
            u = Users(first_name=f_name, last_name = l_name, email = email, 
                      username=uname, password = password, gender = gender)
            
            db.session.add(u)
            db.session.commit()
            return redirect(url_for('home_page'))

        except IntegrityError:
            flash('An error Occured, cannot add signup data to database')
            return redirect('formTester')
    


    return render_template('signup.jinja', form=form)

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