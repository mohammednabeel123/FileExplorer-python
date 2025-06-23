import time
import string
import random
import re
import os
print(os.getcwd())
email_regex = r"^[\w\.-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$"
password_regex = r"^[\w*3\.-]{4,}$"
def username_gen():
    alphabets = string.ascii_lowercase
    numbers = string.digits
    random_alpa = random.choices(alphabets, k=3)
    random_number = random.choices(numbers, k=3)
    alpha_generator = "".join(random_alpa)
    number_generator = "".join(random_number)
    return alpha_generator + number_generator

credentials = {}
def signup():
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")
    if not re.match(email_regex, email_input):
        print("Invalid email format!")
        return
    if not re.match(password_regex, password_input):
        print("Password must be at least 4 characters.")
        return

    print("Generating a username for you...")
    user_name = username_gen()
    print(f"This is your username: {user_name}")

    time.sleep(1)
    credentials[email_input] = (password_input, user_name)
    print("Signup successful!\n")

def signin():
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")
    if not re.match(email_regex, email_input):
        print("Invalid email format!")
        return
    if not re.match(password_regex, password_input):
        print("Invalid password format!")
        return
    if email_input in credentials:
        if password_input == credentials[email_input][0]:
            print("Logging in...")
            time.sleep(1)
            print(f"Welcome back, {credentials[email_input][1]}!")
        else:
            print("Incorrect password.")
    else:
        print("Email not found. Please sign up.")


print("Let's Organize your documents")
print("1.signin\n2.signup")
user_input = input("Enter an option (eg.signin): ").lower()
if user_input == "signin":
    signin()
if user_input == "signup":
    signup()

def information_explorer():
    while True:
        print("\nCurrent Directory:", os.getcwd())
        print("""
        What would you like to do?
        1. Show all files
        2. Show all folders
        3. Show all (files and folders)
        4. Change directory
        5. Exit
        """)
        choice = input(">> ")
