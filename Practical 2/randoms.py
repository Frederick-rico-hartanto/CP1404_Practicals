import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

print(random.randint(1, 100))
print(random.randrange(1, 101, 1))
print(random.uniform(1, 100))

"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

5 is the smallest and 20 is the largest

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?

3 is the smallest and the largest is 9

Could line 2 have produced a 4?

No it cannot be produced, because the step of the range is 2

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

2.5 will be the smallest and 5.5 is the largest

"""