from flask import (Flask, render_template, request, redirect, session, flash, url_for)
from random import randrange

##### Dictionaries "DATABASE"
bank_users = {}

bank_products = {
    "loans" : "",
    "mortgage" : "",
    "credit cards" : ""
}


##### Classes
class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.accounts = []

    def __str__(self):
        return f'''The user: {self.username} has the password: {self.password}. It has {len(self.accounts)} accounts associated with it:'''

    def add_account(self, account_instance: object):
        self.accounts.append(account_instance)

class Account:
    def __init__(self, account_name: str, account_balance: float, account_sort: int, account_number: int):
        self.account_name = account_name
        self.account_balance = account_balance
        self.account_sort = account_sort
        self.account_number = account_number
        self.transactions = []

    def __str__(self):
        return f'''
            The account "{self.account_name}" has £{self.account_balance} as balance.
            The information of the account is:
            + Account number: {self.account_number}
            + Sort code: {self.account_sort}
                '''

    def add_transaction(self,  transaction_instance: object):
        self.transactions.append(transaction_instance)

class Transaction:
    def __init__(self, reference: str, price: float):
        self.reference = reference
        self.price = price

##### Test admin user
def test():
    admin_user = User("admin", "1234")
    main_account = Account("Admin Account", 0.0,
                           randrange(100000, 999999), randrange(10000000, 99999999))
    second_account = Account("Second Account", 0.0,
                             randrange(100000, 999999), randrange(10000000, 99999999))
    transaction1 = Transaction("Greggs", 10.8)
    transaction2 = Transaction("Ikea Furniture", 89.99)
    transaction3= Transaction("Asda Stores", 42.33)
    transaction4 = Transaction("Northumbria Store", 44.99)
    transaction5 = Transaction("Ticket parking Eldon Square", 4.98)

    main_account.add_transaction(transaction1)
    main_account.add_transaction(transaction2)
    main_account.add_transaction(transaction3)
    second_account.add_transaction(transaction4)
    second_account.add_transaction(transaction5)


    admin_user.add_account(main_account)
    admin_user.add_account(second_account)

    bank_users[admin_user.username] = admin_user

    print(f'''{bank_users["admin"]}''')
    for account in bank_users["admin"].accounts:
        print(account.account_name)
test()

##### App
app = Flask(__name__)
app.secret_key = "admin1234"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == "POST":
        username = request.form['username'].lower()
        password = request.form['password']

        if username in bank_users and password == bank_users[username].password:
            session["username"] = bank_users[username].username
            return redirect(url_for("dashboard"))
        else:
            flash('Login failed.')
            return render_template("login.html")

    return render_template("login.html")

@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username'].lower()
        password = request.form['password']

        if username not in bank_users:
            user = User(username, password)
            default_account = Account("Main Account", 0.0, randrange(000000, 999999),randrange(00000000, 99999999))

            user.add_account(default_account)

            bank_users[user.username] = user

            return redirect(url_for("login"))
        else:
            return render_template("register.html")

    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    username = session.get("username")
    return render_template("dashboard.html", user=bank_users[username])

@app.route('/account/<int:account_index>')
def account(account_index):
    username = session.get("username")
    account_selected = bank_users[username].accounts[account_index]

    if account_selected:
        return render_template('account.html', account_selected=account_selected)
    else:
        return "Account not found"


if __name__ == '__main__':
    app.run()