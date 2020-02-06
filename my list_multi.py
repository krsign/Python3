#!usr/bin/env Python3

def multiply(items):
    multiply = 1
    for item in items:
        multiply *= item
    return multiply  #value will be passed to return when calculation is done

print(multiply([1,2,3,4,]))
