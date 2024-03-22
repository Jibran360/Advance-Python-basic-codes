# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# List Comprehension is an elegant way to creat list based on existing lists.

a = [3, 4, 2, 5, 2, 9, 4, 23, 75, 32, 123, 67]

# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

# Shortcut to write the same:
b = [i for i in a if i%2==0]
# b = [i for i in a if i<90]
print(b)


# Set comprehension:
t = [1, 3, 4, 2, 2, 2, 4, 1, 3, 5, 6, 7, 7, 7, 7, 8, 8, 0, 9, 9]
s = {i for i in t}
print(s)