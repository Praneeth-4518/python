def sumofdigs(n):
    sum=0
    while n>0:
        r=n%10
        sum+=r
        n=n//10
    print("sum of digits is:",sum)
sumofdigs(int(input("enter a +ve number:")))    
