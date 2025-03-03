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

items = {
    "watch" : 3.23,
    "soap" : 2.00,
    "television" : 299.99,
    "shoes" : 34.99
}

               
def shopping_basket():
    repeat = True

    while repeat:
        item = input("What item do you want to buy?: ")
        quantity = int(input("How many of them?"))
        answer = input("Do you want to add more? (y/n)")
        if answer == "n":
            repeat = False
    print("Thanks")

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 42 [2 marks]
"""

# DELETE AND REPLACE WITH YOUR ANSWER TO QUESTION 42

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 43 [3 marks]
"""

# DELETE AND REPLACE WITH YOUR ANSWER TO QUESTION 43

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 44 [3 marks]
"""

# DELETE AND REPLACE WITH YOUR ANSWER TO QUESTION 44

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 45 [2 marks]
"""

# DELETE AND REPLACE WITH YOUR ANSWER TO QUESTION 45

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 46 [5 marks]
"""

# DELETE AND REPLACE WITH YOUR ANSWER TO QUESTION 46

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 47 [3 marks]
"""

# DELETE AND REPLACE WITH YOUR ANSWER TO QUESTION 47

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 48 [6 marks]
"""

# DELETE AND REPLACE WITH YOUR ANSWER TO QUESTION 48

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 49 [5 marks]
"""

# DELETE AND REPLACE WITH YOUR ANSWER TO QUESTION 49

"""
------------------------------------------------------------------------------------------------------------------------
QUESTION 50 [10 marks]
"""

# DELETE AND REPLACE WITH YOUR ANSWER TO QUESTION 50