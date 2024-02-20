from flask import Flask , render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, logout_user, login_user, login_required
from flask_migrate import Migrate
from forms import Login, Signup
import pandas as pd
import requests
from models import db, Users, Meal
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
login = LoginManager(app)

login.login_view = 'login'

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))

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

    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    
    form = Login()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()

        if user is None:
            flash('Account not registered')
            return redirect(url_for('sign_up'))
        
        if user is not None and user.verify_password(form.password.data) == False:
            flash('Incorrect Username or Password')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home_page'))
    
    return render_template('login.jinja', form=form)



@app.route('/logout', methods=['POST','GET'])
def logout():
    logout_user()
    flash('You have been logged Out!')
    return redirect(url_for('home_page'))


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

        except SQLAlchemyError as e:
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