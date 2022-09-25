"""
CP1404 Prac 02, Password input with error checking for length.
"""

minimum_password_length = 10

password = input("Password: ")
while len(password) < minimum_password_length:
    print("Invalid password, character length must be 10 or greater.")
    password = input("Password: ")
print("*" * len(password))
