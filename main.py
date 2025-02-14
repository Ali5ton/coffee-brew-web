import sqlite3

from flask import Flask, redirect, render_template, url_for, request
from flask import session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)
app.secret_key = "sfygygw"

######
def get_db():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn

# create tables
def create_tables():
    with get_db() as db:
        db.execute('''CREATE TABLE IF NOT EXISTS user (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    print("Tables created successfully!")


######


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # PK is always unique = primary key
    firstname = db.Column(db.String(), nullable=False)
    secondname = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)



class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)

@app.route("/")
def web():
    return render_template("home.html")

@app.route("/login",methods=['POST','GET'])
def user_signin():
    if request.method == 'POST':
        name = request.form["firstname"]
        surname = request.form["secondname"]
        password = request.form["password"]
        print(name)
        print(surname)
        print(password)
        recording_db = User(firstname=name, secondname=surname, password=password)
        db.session.add(recording_db)
        db.session.commit()
    return render_template('login.html')


@app.route("/signin")
def site():
    return render_template("signin.html")

@app.route("/menu")
def teb():
    return render_template("menu.html")




if __name__=='__main__':
    create_tables()
    app.run(debug=True)

