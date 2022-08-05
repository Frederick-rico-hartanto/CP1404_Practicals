#Basic list operations
# numbers =[]
# for i in range(5):
#     number = int(input("Number: "))
#     numbers.append(number)
#
# # Number: 5
# # Number: 20
# # Number: 1
# # Number: 2
# # Number: 3
# print("The first number is", numbers[0])
# print("The last number is", numbers[-1])
# print("The smallest number is", min(numbers))
# print("The largest number is", max(numbers))
# print("The average of the numbers is", sum(numbers) / len(numbers))


#Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = str(input("Enter username: "))
if username in usernames:
    print("Access granted")
else:
    print("Access denied")