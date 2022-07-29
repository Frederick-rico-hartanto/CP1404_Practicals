# No. 1 and 2
# name = str(input("What is your name: "))
# file = open("name.txt", "w")
# print("Your name is {}".format(name), file=f)
# file.close()

# No. 3 and 4
# file = open("numbers.txt","r")
# num_1 = int(f.readline())
# num_2 = int(f.readline())
# print(num_1 + num_2)
# file.close()

file = open("numbers.txt", "r")
total = 0
for line in file:
    number = int(line)
    total += number
print(total)
file.close()
