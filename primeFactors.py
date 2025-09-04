def primefactors(n):

    for num in range(2,n+1):
        if n%num==0:

            for j in range (2,num):
                if num%j==0:
                    break
            else:
               
                print(num,end=" ")
primefactors(int(input("enter a +ve number:")))                

                