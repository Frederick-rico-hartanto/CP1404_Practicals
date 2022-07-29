"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    random_score = random.randrange(0, 101, 1)
    result = determine_score(score)
    random_result = determine_random_score(random_score)
    print(f"The result of your score is {result}")
    print(f"The random score is {random_score} and the result is {random_result}")


def determine_score(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"

def determine_random_score(random_score):
    if random_score < 0:
        return "Invalid score"
    elif random_score > 100:
        return "Invalid score"
    elif random_score > 90:
        return "Excellent"
    elif random_score >= 50:
        return "Passable"
    elif random_score < 50:
        return "Bad"

main()