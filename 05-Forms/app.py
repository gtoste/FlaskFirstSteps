import math

from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bs4 import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired



app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = '09i8y7bjhnkmlo;p[o09i08u'


class NameForm(FlaskForm):
    userName = StringField('Podaj swoje imie: ', validators=[DataRequired()])
    submit = SubmitField("Wyślij")

class FunctionForm(FlaskForm):
    inputA = IntegerField('Podaj a', validators=[DataRequired()])
    inputB = IntegerField('Podaj b', validators=[DataRequired()])
    inputC = IntegerField('Podaj c', validators=[DataRequired()])
    submit = SubmitField("Wyślij")


@app.route('/')
def index():
    user_form = NameForm()
    return render_template('index.html', title='Strona Główna', userForm=user_form)

@app.route('/user', methods=['POST'])
def user():
    userName = request.form['userName']
    return render_template('user.html', title="Użytkownik", userName=userName)

@app.route('/setSession', methods=['POST', 'GET'])
def setSession():
    userForm = NameForm()
    if userForm.validate_on_submit():
        oldName = session.get('userName')
        if oldName is not None and oldName != userForm.userName.data:
            flash('Wygląda na to, że zmieniłeś imię!')
        session['userName'] = userForm.userName.data
        return  redirect(url_for('setSession'))
    return render_template('session.html', title="Zastosowanie sesji", userForm = userForm, userName = session.get('userName'))

@app.route('/function', methods=['POST','GET'])
def function():

    functionForm = FunctionForm()
    text = ""

    if request.form:
        a = int(request.form['inputA'])
        b = int(request.form['inputB'])
        c = int(request.form['inputC'])

        text = ""
        delta = b * b - 4 * a * c
        if delta > 0:
            x1 = -b + math.sqrt(delta) / 2 * a
            x2 = -b - math.sqrt(delta) / 2 * a
            text = f'Miejsca zerowe funkcji x1={x1} i x2={x2}'
        elif delta == 0:
            x1 = -b / 2*a
            text = f'Miejsce zerowe funkcji x1={x1}'
        else:
            text = f'Brak miejsc zerowych'

    return render_template('function.html', title='Funkcja kwadratowa', functionForm = functionForm, result = text)

if __name__=='__main__':
    app.run(debug=True)
