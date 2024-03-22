l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 34, 55, 75, 89, 98, 90, 50]

a = filter(lambda a: a%5==0, l)     # Numbers divisible by 5
print(list(a))