def delpos():
    l=[1,2,3,4,5]
    pos=3
    for i in range(pos-1,4):
        l[i]=l[i+1]
    l.pop()    
    print(l)    
delpos()    