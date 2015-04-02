#!/usr/bin/env python

def print_arg(name, arg):
    print "{name}: {argument}".format(name=name, argument=arg)








def named_parameters_default_value(candy, corn, cats="KITTENS!!"):

    print "named parameters: "

    print_arg('candy', candy)
    print_arg('corn', corn)
    print_arg('cats', cats)

named_parameters_default_value('sucker', 'maize')
