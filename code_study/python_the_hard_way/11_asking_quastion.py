#!/usr/bin/python
# -*- coding: utf-8 -*-

# raw_input - была переименована в (input) с python 3.0

print ('How old are you?'),
age = input()
print ('How tall are you?'),
height = input()
print ('How much do you weight?'),
weight = input()
print ("So, you're %r old, %r tall and %r heavy." % (age, height, weight))