def fact(n):
    fact=1
    i=n
    while i>=1:
        fact=fact*i
        i=i-1
    print(f"fact of {n} is {fact}")    
fact(int(input("enter a +ve number:")))    