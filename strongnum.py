def strongnum(m):
              for n in range(1,m+1):
                  sum=0
                  temp=n
                  while n>0:
                      fact=1
                      digit=n%10
                      i=digit
                      while i>=1:
                          fact=fact*i
                          i=i-1
                      sum=sum+fact
                      n=n//10
                  if sum==temp:
                      print(temp,end=" ")
strongnum(int(input("enter a +ve number:")))                      