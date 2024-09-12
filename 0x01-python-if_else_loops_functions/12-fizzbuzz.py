#!/usr/bin/python3
def fizzbuzz():
    for numb in range(1, 101):
        mult_three = 3 * numb
        mult_five = 5 * numb
        if numb == mult_three:
            print('{}'.format("Fizz"), end=" ")
        elif numb == mult_five:
            print('{}'.format("Buzz"), end=" ")
        elif numb == mult_three and numb == mult_five:
            print('{}'.format("fizzbuzz"), end=" ")
        else:
            print('{}'.format(numb), end=" ")
