"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    random_score = random.randrange(0, 101, 1)
    result = determine_score(score, random_score)
    print(f"The random score is {random_score} and the result is {result}")
    print(result)

def determine_score(score, random_score):
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

main()