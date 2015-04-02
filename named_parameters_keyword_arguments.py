#!/usr/bin/env python

def print_arg(name, arg):
    print "{name}: {argument}".format(name=name, argument=arg)











def named_arguments(candy, corn, cats):

    print "named parameters: "

    print_arg('candy', candy)
    print_arg('corn', corn)
    print_arg('cats', cats)

print "Called with all keyword arguments: "
named_arguments(corn='maize', candy='sucker', cats='four legged')

print "Called with some keyword and some not: "
named_arguments('sucker', cats='four legged', corn='maize')

