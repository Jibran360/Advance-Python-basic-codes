from functools import reduce

l = [3, 8, 4, 2, 5, 7, 9, 12, 23, 21]

a = reduce(max, l)
print(a)