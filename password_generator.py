import random
from string import lowercase
from string import uppercase
from string import digits
from string import punctuation

count_lowercase = int(raw_input("Enter how much lowercase letters should be in your password: "))
count_uppercase = int(raw_input("Enter how much uppercase letters should be in your password: "))
count_digits = int(raw_input("Enter how much digits should be in your password: "))
count_symbols = int(raw_input("Enter how much symbols should be in your password: "))

def password_generator():
    password = []

    for i in range(count_lowercase):
        password.append(random.choice(lowercase))

    for i in range(count_uppercase):
        password.append(random.choice(uppercase))

    for i in range(count_digits):
        password.append(random.choice(digits))

    for i in range(count_symbols):
        password.append(random.choice(punctuation))

    random.shuffle(password)
    print "Your password is: " + "".join(password)

password_generator()
