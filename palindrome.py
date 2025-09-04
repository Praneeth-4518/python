def palindrome(m):
    for n in range(1,m+1):
        rev=0
        temp=n
        while n>0:
            digit=n%10
            rev=rev*10+digit
            n=n//10
        if rev==temp:
            print(temp,end=" ")
          
palindrome(int(input("enter a +ve number:")))     