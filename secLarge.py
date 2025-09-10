def secLarge():
    l=[6,3,4,2,5]
    max=0
    secmax=0
    for i in l:
        if i>max:
            max=i
    for i in l:
        if i!=max and i>secmax :
            secmax=i  
    print(secmax) 
    print(max)              
secLarge()    
