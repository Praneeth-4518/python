def firstNlast(n):
    first=n
    last=n%10
    while first>=10:
        first=first//10
    print("first digit is:",first)
    print("last digit is:",last)  
firstNlast(int(input("enter a +ve number:")))      