#!/usr/bin/python3
str1 = "Fizz"
str2 = "Buzz"


def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 == 0 and number % 5 == 0):
            print("%s%s" % (str1, str2), end=' ')
        elif (number % 3 == 0):
            print("%s" % (str1), end=' ')
        elif (number % 5 == 0):
            print("%s" % (str2), end=' ')
        else:
            print("%d" % (number), end=' ')
