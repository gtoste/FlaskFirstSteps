from flask import Flask, render_template, request
from flask_bs4 import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = '09i8y7bjhnkmlo;p[o09i08u'


class NameForm(FlaskForm):
    userName = StringField('Podaj swoje imie: ', validators=[DataRequired()])
    submit = SubmitField("Wyślij")


@app.route('/')
def index():
    user_form = NameForm()
    return render_template('index.html', title='Strona Główna', userForm=user_form)

@app.route('/user', methods=['POST'])
def user():
    userName = request.form['userName']
    return render_template('user.html', title="Użytkownik", userName=userName)

if __name__=='__main__':
    app.run(debug=True)
