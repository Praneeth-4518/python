def num2word(n):
    l=[]
    while n>0:
        r=n%10
        if r==0:
            l.append("zero")
        elif r==1:                                  
            l.append("one")
        elif r==2:  
            l.append("two")
        elif r==3:                                  
            l.append("three")
        elif r==4:  
            l.append("four")    
        elif r==5:  
            l.append("five")
        elif r==6:  
            l.append("six")
        elif r==7:
            l.append("seven")
        elif r==8:  
            l.append("eight")
        elif r==9:
            l.append("nine")
        n=n//10
    l.reverse()
    for i in l:
        print(i,end=" ") 
num2word(int(input("enter a +ve number:")))        