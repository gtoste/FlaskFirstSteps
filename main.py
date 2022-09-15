from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>witaj</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Witaj {name}'

if __name__=='__main__':
    app.run()

