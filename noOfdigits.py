def digits(n):
    count=0
    while n>0:
        
        count+=1
        n=n//10
    print("no of digits is:",count)
digits(int(input("enter a +ve number:")))    
