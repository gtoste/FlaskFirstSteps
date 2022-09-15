from flask import Flask, render_template
from flask_bs4 import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html', title='Strona Główna')

@app.route('/user/<name>')
def user(name):
    return render_template('index.html', title='użytkownik', name=name)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html', title='404'), 404

@app.errorhandler(500)
def pageNotFound(error):
    return render_template('500.html', title='500'), 500

if __name__=='__main__':
    app.run()
