#!/usr/bin/env python

import sys
sys.setrecursionlimit(10008)

def fibonacci_cached(number, known_values=[]):
    if known_values == []:
        print "values are not cached"
        known_values = [0] * 10000


    if number <= 1:
        return number
    else:
        if(known_values[number - 1] == 0):
            known_values[number - 1] = fibonacci_cached(number - 1)

        if(known_values[number - 2] == 0):
            known_values[number - 2] = fibonacci_cached(number - 2)

        known_values[number] = known_values[number - 1] + known_values[number - 2]

        return known_values[number]

def main():
    number = None
    while number != 1:
        print('Enter a number : ')
        number = int(sys.stdin.readline())
        print(fibonacci_cached(number))
        print "    "
        print "    "

if __name__=='__main__':
    main()
