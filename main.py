from pywebio.input import *
from pywebio.output import *

#Dictionaries, this is a comment
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

    def __init__(self, username, password, meetings, dob, str):
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


def login():
    put_text("This is the login page")
    button("Go to second page", onclick=lambda: push(second_page))

def register():
    put_text("This is the register page")

if __name__ == '__main__':
    login()

