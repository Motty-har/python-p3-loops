#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i in range(10, 0, -1):
        print(i)
        i -= 1 
    
    print("Happy New Year!")
    pass

def square_integers(int_list):
    return [int **2 for int in int_list]
    pass

def fizzbuzz():
    i = 0
    while i in range(0, 100, 1):
        i += 1
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
    pass
