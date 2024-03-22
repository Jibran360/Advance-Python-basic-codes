# def func(a):
#     return a+5

func = lambda a: a+5
square = lambda x: x*x
sum = lambda a, b, c: a+b+c

x = 4
print(func(x))  # Returns 9
print(square(x)) # Returns 16
print(sum(x, 1, 3)) # Return 8
