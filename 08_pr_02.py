name = input("Enter your name: ")
marks = input("Enter your marks: ")
phone = input("Enter your phone Number: ")

'''format method (strings)
   formats the values inside the string into a desired output
    template.format(p1,p2...)'''

template = "The name of the student is {}, his marks are {} and phone number is {} ".format(name, marks, phone)
# output = template.format(name, marks, phone)
print(template)