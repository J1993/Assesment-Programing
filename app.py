from random import random, randrange

from flask import Flask, render_template, request

#Dictionaries
bank_users = {
    "admin" : {
        "password" : "admin1234",
        "accounts" : {
            "Current Account": {
                "account-balance" : 1642.83,
                "account-sort" : 112233,
                "account-number" : 654321,
            }
        }
    }
}

user_transactions = {
    "admin" : {
        "Northumbria Coffee Shop": 2.30,
        "KFC Newcastle": 14.99
    }
}

bank_products = {
    "loans" : "",
    "mortgage" : "",
    "credit cards" : ""
}


#Classes
class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accounts = {
            "account-1": {
                "account-name" : "Main Account",
                "account-balance" : 0.0,
                "account-sort" : 0,
                "account-number" : 0,
            }
        }

class Transactions(User):
    def __init__(self, reference, quantity, username, password):
        super().__init__(username, password)
        self.reference = reference
        self.quantity = quantity


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def login():

    #Here we request from the login form in the html template the details to try the login.
    if request.method == "POST":
        username = request.form['username'].lower()
        password = request.form['password']

        if username in bank_users and password == bank_users[username]["password"]:
            return render_template("dashboard.html", user=bank_users[username], username=username)

    return render_template("login.html")

@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username'].lower()
        password = request.form['password']

        if username not in bank_users:
            user = User(username, password)
            bank_users[user.username] = {"password" : user.password, "accounts" : {"Current Account" : {"account-balance" : 0.0, "account-sort" : randrange(100000,999999), "account-number" : randrange(100000, 999999),}}}
            print(bank_users[user.username])
            return render_template("index.html")

    return render_template("register.html")

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():

    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run()
