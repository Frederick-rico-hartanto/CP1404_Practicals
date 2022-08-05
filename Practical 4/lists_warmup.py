numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0]
numbers[-1]
numbers[3]
numbers[:-1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]

#Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(numbers[0])

#Change the last element of numbers to 1
numbers[-1] = 1
print(numbers[-1])

#Get all the elements from numbers except the first two (slice)
print(numbers[2:])

#Check if 9 is an element of numbers
if 9 in numbers:
    print("Yes 9 is in list")
else:
    print("No 9 not in list")