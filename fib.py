#!/usr/bin/env python

import sys


def fibonacci(number, **kwargs):
    if number == 1:
      return 1
    elif number == 0:
        return 0
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

def main():
    number = None
    while number != 1:
        print('Enter a number : ')
        number = int(sys.stdin.readline())
        print(fibonacci(number))
        print "    "
        print "    "

if __name__=='__main__':
    main()

