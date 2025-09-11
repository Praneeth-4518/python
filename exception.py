def exph():
    try:
        x=int(input("Enter a number 1: "))
        y=int(input("Enter a number 2: "))
        z=x/y
        print(z)
    except:
        print("Error: Division by zero is not allowed.")
    else:
        print("Division performed successfully.")
exph()        
