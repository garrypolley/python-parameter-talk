#!/usr/bin/env python


def print_arg(name, arg):
    print "{name}: {argument}".format(name=name, argument=arg)


def kwargs_stuff(candy, corn, cats='CATS', **kwargs):

    print "named parameters: "

    print_arg('candy', candy)
    print_arg('corn', corn)
    print_arg('cats', cats)

    for key, value in kwargs.iteritems():
        print key, value

    print

extras = {'one': 1, 'two': 2, 'three': 3}
kwargs_stuff('sucker', 'maize', 'four legged', **extras)

kwargs_stuff('sucker', 'maize', one=100, two=200, three=300)
