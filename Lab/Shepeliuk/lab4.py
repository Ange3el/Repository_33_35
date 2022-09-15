#Task 1-3
# A = {3, 5, 11, 7, 4, -3}
# B = {11, 5, 8, 1, 10, 7}
# commonEl = A & B
# differentEl = A - B
# association = A | B
# print(commonEl)
# print(differentEl)
# print(association)

#Task 4
# arr ="a14b6fa"
# setarr = set(arr)
# if len(arr) == len(setarr):
#     print("Всі елементи унікальні")
# else:
#     print("Є одинакові")

#Task 5
from ast import operator
from collections import Counter
dict = { 1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Sat', 6:'Sat', 7:'Sun' }
values = list(dict.values())
count = operator.countOf(values, )