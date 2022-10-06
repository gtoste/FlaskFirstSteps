import math

from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bs4 import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.config['SECRET_KEY'] = '09i8y7bjhnkmlo;p[o09i08u'
bootstrap = Bootstrap(app)

class ListForm(FlaskForm):
    list = StringField('Wpisz dowolny ciąg znaków: ', validators=[DataRequired()])
    submit = SubmitField("Wyślij")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ListForm()


    if request.form:
        list = request.form['list'].split(',')
        sum = 0
        for e in list:
            e = float(e.strip())
            sum = sum + e

        if len(list) > 0:
            list.sort(reverse=True)
            list_sorted = ",".join(list)
            max = list[0]
            min = list[-1]
            avg = sum / len(list)
            return render_template('index.html', title="Zadanie 2.1", form=form, list_sorted=list_sorted, min=min,
                                   max=max, avg=avg)

    return render_template('index.html', title="Zadanie 2.1", form=form)


if __name__=='__main__':
    app.run()
