from json.tool import main


def greet(name):
    print(f"Good morning, {name}")

if __name__ == '__main__':    # __name__ evaluates to the name of the module in python from where the progam is run
    
    n = input("Enter a name:\n")
    greet(n)