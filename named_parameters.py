#!/usr/bin/env python

def print_arg(name, arg):
    print "{name}: {argument}".format(name=name, argument=arg)









def named_arguments(candy, corn, cats):

    print "named parameters: "

    print_arg('candy', candy)
    print_arg('corn', corn)
    print_arg('cats', cats)

named_arguments('sucker', 'maize', 'four legged')
