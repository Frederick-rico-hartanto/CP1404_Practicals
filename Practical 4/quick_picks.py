import random

NUMBER_IN_LINE = 6
MIN = 1
MAX = 45


number_of_quick_picks = int(input("How many quick picks? "))
while number_of_quick_picks < 0:
    print("Invalid number")
    number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBER_IN_LINE):
        number = random.randint(MIN, MAX)
        while number in quick_pick:
            number = random.randint(MIN, MAX)
        quick_pick.append(number)
    quick_pick.sort()

    print(" ".join("{:2}".format(number) for number in quick_pick))