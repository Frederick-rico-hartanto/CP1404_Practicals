def main_1():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

def main_2():
    for i in range(0, 110, 10):
        print(i, end =' ')
    print()

def main_3():
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

def main_4():
    number_of_stars = int(input("Number of star: "))
    for i in range(number_of_stars):
        print("*", end='')

def main_5():
    number_of_stars = int(input("Number of star: "))
    for i in range(number_of_stars):
        for n in range(i+1):
            print("*", end='')
        print()

main_5()