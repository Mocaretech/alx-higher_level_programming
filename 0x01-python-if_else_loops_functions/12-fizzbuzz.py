#!/usr/bin/python3
def fizzbuzz():
    for numb in range(1, 101):
        mult_three = numb % 3
        mult_five = numb % 5
        if numb == mult_three:
            print('Fizz', end=" ")
        elif numb == mult_five:
            print("Buzz", end=" ")
        elif numb == mult_three and numb == mult_five:
            print("fizzbuzz", end=" ")
        else:
            print('numb', end=" ")
