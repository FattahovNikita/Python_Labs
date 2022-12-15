from pyDatalog import pyDatalog
from random import randint

pyDatalog.create_terms('X, Sum, Average, median, Median, arr, mult, Mult')

# Сумма ряда
Sum[X] = ((1 + X) * X) / 2
print("Sum 1-999999:")
print(Sum[999999] == X)