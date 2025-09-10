def evenodd():
    l=[1,2,3,4,5]
    ec=0
    oc=0
    for i in l:
        if i%2==0:
            ec+=1
        else:
            oc+=1
    print(f"no.of even and odd nums in list are {ec} and {oc} respectively") 
evenodd()               