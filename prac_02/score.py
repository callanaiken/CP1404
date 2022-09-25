"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = int(input("Enter score: "))
    print(f"You're score is: {determine_comment(score)}")

    random_number = random.randint(0, 100)
    print(f"The random score is: {random_number}")
    print(f"Random score is: {determine_comment(random_number)}")


def determine_comment(score):
    if score < 0:
        comment = "Invalid score"
    elif score < 50:
        comment = "Bad"
    elif score < 90:
        comment = "Passable"
    elif score < 100:
        comment = "Excellent"
    else:
        comment = "Invalid score"
    return comment


main()
