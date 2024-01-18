# Chapter 02
#
# This is a crash course in Python elements
# that we will be using in this enviornment.

# This is a space to play with the functions and aspects
# of Python
# None of this should be kept, but you can play
# around in this file.

import re
from collections import defaultdict, Counter


# LISTS

long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13
                           + 14 + 15 + 16 + 17 + 18 + 19 + 20)

lists_of_lists = [(1, 2, 3),
                  (4, 5, 6),
                  (7, 8, 9)]

print(lists_of_lists)

my_regex = re.compile("[0-9]+", re.I)
print(my_regex)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
x[0] = -1

print(zero, "\n", one, "\n", nine, "\n", eight, "\n", x[0])

list2 = [zero, one, nine, eight, x]

print(list2)

# TUPLES
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3
print(my_list[1])

try:
    my_tuple[1] = 3
except TypeError:
    print("Cannot modify a tuple.")

def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2,3)
print("SP: ", sp)