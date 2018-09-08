from flask import Flask, render_template, Blueprint, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import Events

app = Flask(__name__)
auth = Blueprint('auth',__name__)
app.secret_key = 'asdfkn50cv8ZDF#$%'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://sqlwr:Innovation@192.168.1.189/NOA'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()

@app.route("/")
def hello():
    test = db.session.query(Events).all()
    print(test)
    return render_template('index.html')

@app.route("/moop")
def moop():
    return "moop"
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
