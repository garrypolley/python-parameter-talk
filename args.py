#!/usr/bin/env python


def print_arg(name, arg):
    print "{name}: {argument}".format(name=name, argument=arg)


def kwargs_stuff(candy, corn, cats='CATS', *args):

    print "named parameters: "

    print_arg('candy', candy)
    print_arg('corn', corn)
    print_arg('cats', cats)

    for value in args:
        print value

    print

extras = {'one': 1, 'two': 2, 'three': 3}
kwargs_stuff('sucker', 'maize', 'four legged', *extras.keys())

kwargs_stuff('sucker', 'maize', 'override cat', 200, 300)
