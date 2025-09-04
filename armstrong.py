def armstrong(m):
    for n in range(1,m+1):
        
        sum=0
        temp=n
        while n>0:
            r=n%10
            sum=sum+r**3
            n=n//10 
        if sum==temp:
            print(temp,end=" " )
armstrong(int(input("enter a +ve number:")))          