def sets():
    d1=["soulhitter45@gmail.com","praneethnalla045@gmail.com","hitman45@gmail.com","soulhitter45@gmail.com"]
    d2=["soulhitter45@gmail.com","praneethnalla045@gmail.com","kohli18@gmail.com"]
    d3=["soulhitter45@gmail.com","hardik33@gmail.com","kl1@gmail.com"]
    
    print(set(d1))
    print(set(d2))
    print(set(d3))
    print("2---------------------------------------------------------------")
    count=0
    for i in d1:
        if i not in d2 and i not in d3:
            count+=1
    for i in d2:
        if i not in d1 and i not in d3:
            count+=1  
    for i in d3:
        if i not in d1 and i not in d2:
            count+=1
    print(count)
    print("3---------------------------------------------------------------")
    print((set(d1).intersection(set(d2))).intersection(set(d3))) 
    print("4---------------------------------------------------------------")       
    print(set(d1))
    print(set(d2))
    print(set(d3))

    l2=[]
    for i in d1:
        if i not in d2 and i not in d3:
            l2.append(i)
    for i in d2:
        if i not in d1 and i not in d3:
            l2.append(i)  
    for i in d3:
        if i not in d1 and i not in d2:
            l2.append(i)
    print(l2) 
    print("5---------------------------------------------------------------")
    print((set(d1).intersection(set(d2))),"  ",(set(d2).intersection(set(d3))), "  ",(set(d1).intersection(set(d3))))
    
    


sets()