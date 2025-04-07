from flask import (Flask, render_template, request)
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
        return f'''
            The user: {self.username} has the password: {self.password}.
            It has {len(self.accounts)} accounts associated with it.
                '''

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
    def __init__(self, reference, quantity):
        self.reference = reference
        self.quantity = quantity

##### Test admin user
admin_user = User("admin", "1234")
main_account = Account("Admin Account", 0.0, randrange(100000, 999999),randrange(10000000, 99999999))
second_account = Account("Second Account", 0.0, randrange(100000, 999999),randrange(10000000, 99999999))

admin_user.add_account( main_account)
admin_user.add_account(second_account)

bank_users[admin_user.username] = admin_user

print (f'''{bank_users["admin"]}''')
for account in bank_users["admin"].accounts:
    print(account.account_name)


##### App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    #Request from the login form in the html template the details to try the login.
    if request.method == "POST":
        username = request.form['username'].lower()
        password = request.form['password']

        #Validation of the inputs by checking if they exist in the database
        if username in bank_users and password == bank_users[username].password:
            #If the information exists, it will render the dashboard page sending the user instance to the new page.
            return render_template("dashboard.html", user=bank_users[username])

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

            return render_template("login.html")

    return render_template("register.html")

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():

    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run()
