def unique():
    l=[1,2,3,4,5,2,4]
    
    for i in range(7):
        for j in range(7):
            if  j!=i and l[i]==l[j]:
                break
        else:
            print(l[i])
unique()                
