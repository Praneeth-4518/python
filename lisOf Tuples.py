def lot():
    l=[('Rohit',45),('kohli',18),('bumrah',93),('hardik',33),('kl',1)]
    max=0
    smax=0
    name=""
    for i in l:
        
        if int(i[1])>max:
            max=i[1]
    for i in l:
        if int(i[1])!=max and int(i[1])>smax:
            smax=i[1]
            name=i[0]
    print(name,"got second max marks ->",smax)            
    for i in l:
        if int(i[1])>75:
            print(i[0] ,"got hightest marks -> ",i[1])
    
    
lot()    
      