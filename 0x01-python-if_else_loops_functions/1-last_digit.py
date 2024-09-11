#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = number % 10
result = f"Last digit of {number} is {Last_digit}"
if Last_digit > 5:
    print(f"{result} and is greater than 5")
elif Last_digit == 0:
    print(f"{result} and is 0")
elif Last_digit < 6 and Last_digit != 0:
    print(f"{result} and is less than 6 and not 0")
