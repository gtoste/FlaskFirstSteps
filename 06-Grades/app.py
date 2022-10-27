import json

from flask import Flask, render_template, session, redirect
from flask_bs4 import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
date = datetime.now()
app.config['SECRET_KEY'] = '09i8y7bjhnkmlo;p[o09i08u'


class LoginForm(FlaskForm):
    userLogin = StringField('Nazwa użytkownika:', validators=[DataRequired()])
    userPass = PasswordField('Hasło:', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')

users = {
    1 : {
        "userLogin": "mPanek",
        'userPass' : 'Qwerty123!',
        'fname' : 'Mateusz',
        'lname' : 'Panek'
    }
}


@app.route('/')
def index():
    return render_template('index.html', title='Strona Główna')

@app.route('/logIn', methods=['POST','GET'])
def logIn():
    login = LoginForm()
    if login.validate_on_submit():
        userLogin = login.userLogin.data
        userPass = login.userPass.data
        if userLogin == users[1]['userLogin'] and userPass == users[1]['userPass']:
            session['userLogin'] = userLogin
            return redirect('dashboard')
    return render_template('login.html', title="Logowanie", login =login, userLogin=session.get('userLogin'))

@app.route('/dashboard')
def dashboard():
    with open('data/grades.json','r') as f:
        grades = json.load(f)
    return render_template('dashboard.html', title='Dashboard', userLogin=session.get('userLogin'), date = date, grades = grades)

@app.route('/logOut')
def logOut():
    session.pop('userLogin')
    return redirect('logIn')

if __name__=='__main__':
    app.run(debug=True)
