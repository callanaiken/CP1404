"""
CP1404 Prac 02, Score Menu
"""

MENU = """E - Enter score
R - Display results for entered score
S - Display a number of stars equal to the score
Q - Quit program
"""


def main():
    score = 0
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "E":
            score = get_valid_input("Score: ", 0, 100)
        elif choice == "R":
            print(determine_result(score))
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("> ").upper()
    print("Farewell")


def get_valid_input(prompt, lowest_value, highest_value):
    value = int(input(prompt))
    while value < lowest_value or value > highest_value:
        print(f"Invalid score, type a number between {lowest_value} and {highest_value}")
        value = int(input(prompt))
    return value


def determine_result(value):
    if value < 50:
        result = "Bad"
    elif value < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
