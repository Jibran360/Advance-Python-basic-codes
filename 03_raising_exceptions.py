def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Saad")

a = increment(int(input("Enter value: ")))
print(a)


