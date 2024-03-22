def square(num):
    return num*num 

l = [1, 2, 4]

# Method 1
l2 = []
for item in l:
    l2.append(square(item))
print(l2)

# Method 2
''' map applies a function to all the items in an input_list
     Syntax:     map(function, input_list) 
    Filter creates a list of items for which the function returns true
                 list(filter(function, l) '''

print(list(map(square, l)))      # Works as well as method 1

