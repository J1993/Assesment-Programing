"""
Use this python file as a template for your work
Questions are listed in the PDF in the assessment area
Make sure that it is clear which answer goes with which question
When you are finished copy and paste the whole script below and paste into the Assessment form on Blackboard
"""

# COPY FROM THE LINE BELOW THIS ONE TO THE END AND PASTE INTO BLACKBOARD
"""
QUESTION 0
Set the variable my_student_id to your student ID.
[0 marks]
"""

my_student_id = "18033447"

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 1 [1 mark]
"""

print("Lopez Zapata")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 2 [1 mark]
"""

first_name = "Oscar Jordy"

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 3 [1 mark]
"""

age = 31

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 4 [1 mark]
"""

print(f"My name is {first_name} and I am {age} years old")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 5 [1 mark]
"""

sentence = "This is a programming assessment"
print(f"The string's length is {len(sentence)}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 6 [1 mark]
"""

days_of_week  =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_week[-1])

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 7 [1 mark]
"""

script = input("Insert your text: ")
print(script[::-1])

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 8 [1 mark]
"""

number1 = 23
number2 = 10
result = number1 - number2
print(f"The answer is {result}")
"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 9 [1 mark]
"""

number1 = 10
number2 = 160
result2 = number2 / number1
print(f"The answer is {result2}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 10 [1 mark]
"""

number1 = 10
number2 = 2
num3 = 5
result3 = (number1 * number2) / num3
print(f"The answer is {result3}")


"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 11 [2 marks]
"""

number1 = 24
number2 = 4
num3 = 2
result4 = (number1 - number2) ** num3
print(f"The answer is {result4}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 12 [2 marks]
"""

number_input = int(input("Insert your number: "))
result = number_input * 100
print(f"The answer is {result}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 13 [2 marks]
"""

area1 = int(input("Insert your first area: "))
area2 = int(input("Insert your second area: "))
result = area1 * area2
print(f"The area is {result}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 14 [2 marks]
"""
number1 = int(input("Insert your first number: "))
number2 = int(input("Insert your second number: "))
number3 = int(input("Insert your third number: "))
average = (number1 + number2 + number3) / 3
print(f"The average is {average}")
"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 15 [1 mark]
"""

import math

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 16 [1 mark]
"""

number = 14.8
result = math.floor(number)
print(f"The number floored is {result}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 17 [1 mark]
"""

number = 34
result = math.sqrt(number)
print(f"The square root is {result}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 18 [1 mark]
"""

text = input("Insert your text: ")
print(f"The length of thi string is {len(text)}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 19 [2 marks]
"""

name = input("Insert your name: ")
nickname = input("Insert your nickname: ")
length = len(name) - len(nickname)
print(f"Your name is {length} letters longer than your nickname")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 20 [1 mark]
"""

password = input("Insert your password: ")
if len(password) < 12:
    print("Password is too short")
else:
    print("Password updated")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 21 [1 mark]
"""

number = int(input("Insert your number to know if is odd or even: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 22 [2 marks]
"""
answer = input("It is rainig? [Y/N]: ").lower()
if answer == "y":
    is_rainig = True
elif answer == "n":
    is_rainig = False

if is_rainig:
    print("Better take an umbrella")
else:
    print("Clear Skies")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 23 [2 marks]
"""
dictionary = {
    "Crisps" : "1.20",
    "Cola" : "2.5",
    "Candy" : "0.72"
}

print(f"The price of a cola is: £{dictionary["Cola"]}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 24 [1 mark]
"""

mark = int(input("Insert your mark: "))
if mark >= 40:
    print("Pass")
else:
    print("Fail")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 25 [2 marks]
"""
mark = int(input("Insert your mark out of 100: "))

if mark < 40:
    print("Grade F")
elif mark >= 40 and mark < 60:
    print("Grade C")
elif mark >= 60 and mark < 80:
    print("Grade B")
else:
    print("Grade A")


"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 26 [1 mark]
"""

for number in range(10, -1, -1):
    print("Lift off!") if number == 0 else print(number)

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 27 [1 mark]
"""

total = 0
for number in range(1, 25, 1):
    total = total + number

print(f"The total is {total}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 28 [2 marks]
"""

user_number = int(input("Insert a number: "))
number_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in number_set:
    total = user_number * n
    print(f"{user_number} x {n} = {total}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 29 [1 mark]
"""

string = "Hola is Hi in English"

for char in string:
    print(char)

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 30 [1 mark]
"""

sensible_name = [2, 4, 6, 8, 10, 12, 14, 16]
new_list = []

for number in sensible_name:
    new_number = number + 4
    new_list.append(new_number)
print(new_list)

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 31 [1 mark]
"""

strings = ["Hola", "is", "Hi", "in Spanish"]
new_string = " ".join(strings)

print(new_string)

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 32 [2 marks]
"""

list = [1, 2, 3, 4, 5]
new_list = []

for number in list:
    number = number ** 2
    new_list.append(number)
print(new_list)

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 33 [2 marks]
"""

list = [8, 2, 18, 19, 48, 3]
list.sort(reverse=True)
print(list[0])

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 34 [2 marks]
"""

dictionary = {
    "Jordy" : "jordylopez@northumbria.com",
    "Josh" : "joshbrown@northumbria.com",
    "Jordan" : "michaeljordan@northumbria.com"
}
print(f"The email of Jordan is {dictionary["Jordan"]}")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 35 [1 mark]
"""

def welcome_user():
    print("Welcome user")

welcome_user()

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 36 [1 mark]
"""

def adds_two_numbers(num1, num2):
    print(num1 + num2)

adds_two_numbers(1, 2)

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 37 [1 mark]
"""

def capitalize(str):
    capital = str.capitalize()
    print(capital)

capitalize("hola")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 38 [3 marks]
"""

def contains_a(str):
    if 'a' in str:
        return True
    else:
        return False

print(contains_a("Nomo"))

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 39 [3 marks]
"""

def it_matchs(string1, string2):
    if string1 == string2:
        print("Matchs!")
    else:
        print("Error")

it_matchs("Hola", "Hola")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 40 [3 marks]
"""

def even_numbers(number):
    list = []
    for number in range(0, number, 1):
        if number % 2 == 0:
            list.append(number)
    print(list)

even_numbers(53)


"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 41 [3 marks]
"""

def shopping_basket():
    basket = {}
    repeat = True

    while repeat:
        item = input("What item do you want to buy?: ")
        quantity = int(input("How many of them?"))
        basket.update({item: quantity})
        answer = input("Do you want to add more? (y/n)")
        if answer == "n":
            repeat = False
    print(basket)

shopping_basket()

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 42 [2 marks]
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 43 [3 marks]
"""

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Student name: {self.name} and student ID: w{self.student_id}"

student = Student("Jordy Lopez", "18033447")
print(student)

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 44 [3 marks]
"""

class Patient:
    def __init__(self, name, age, isvaccinated):
        self.name = name
        self.age = age
        self.isvaccinated = isvaccinated

    def __str__(self):
        if self.isvaccinated:
            return f"{self.name} is {self.age} years old and is vaccinated"
        else:
            return f"{self.name} is {self.age} years old is not vaccinated"



patient1 = Patient("Patient 1", 25, False)
print(patient1)
patient1.isvaccinated = True
print(patient1)

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 45 [2 marks]
"""

class OutPatient(Patient):
    def __init__(self, discharge_date):
        self.discharge_date = discharge_date

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 46 [5 marks]
"""


class Player:
    name = ""
    role = ""
    points = 0
    health = 100
    inventory = []

    def __init__(self, name, role, points, health, inventory):
        self.name = name
        self.role = role
        self.points = points
        self.health = health
        self.inventory = inventory

    def add_points(self, points):
        self.points += points

    def takes_damage(self, damage):
        self.health -= damage

    def add_inventory(self, item):
        self.inventory.append(item)

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 47 [3 marks]
"""

attempts = 0
password = "1234HiBen"

while attempts < 3:
    user_password = input("Enter password: ")

    if user_password == password:
        print("Succesfully Logged")
        break
    elif attempts == 2:
        print("Account Locked")
        break
    else:
        print("Wrong password")
        attempts += 1

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 48 [6 marks]
"""

balance = 100
pin = 1234
user_pin = 0000
start = True

while pin != user_pin:
    user_pin = int(input("Enter Pin: "))

while start:
    print("Select Service:")
    display_balance = input("- Display Balance?: [y/n]")

    if display_balance == "n":
        withdraw_funds = input("- Withdraw funds?: [y/n]")
        if withdraw_funds == "n":
            cancel = input("- Cancel transaction?: [y/n]")
            if cancel == "y":
                start = False
        else:
            amount = int(input("Enter amount: "))
            if amount > balance:
                print("Insufficient funds")
            else:
                balance = balance - amount
                print("Dispensing Cash")
                print(f"Your new balance is £{balance}")
                start = False
    else:
        print(f"You have £{balance} left")

print("Returning Card")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 49 [5 marks]
"""

start = True
username = ""
password = ""

while start:

    option = int(input("""
### User Management ###

1 - Create a new username and password.
2 - Update username.
3 - Update password.
4 - Log off.

Select an option:"""))
    if option == 1:
        username = input("Username: ")
        password = input("Password: ")
        print("> User created successfully.")
    elif option == 2:
        if username == "":
            print("> No username found. Add a new username and password before updating")
        else:
            username = input("New Username: ")
            print("> Username updated successfully.")
    elif option == 3:
        if password == "":
            print("> No password found. Add a new username and password before updating")
        else:
            password = input("New password: ")
            print("> Password updated successfully.")
    else:
        start = False
print("### Log Off ###")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 50 [10 marks]
"""

# DELETE AND REPLACE WITH YOUR ANSWER TO QUESTION 50