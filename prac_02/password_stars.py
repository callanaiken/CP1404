"""
CP1404 Prac 02, Password input with error checking for length.
"""


def main():
    minimum_password_length = 10

    password = get_password(minimum_password_length)
    display_password(password)


def display_password(password):
    print("*" * len(password))


def get_password(minimum_password_length):
    password = input("Password: ")
    while len(password) < minimum_password_length:
        print("Invalid password, character length must be 10 or greater.")
        password = input("Password: ")
    return password


main()
