def dup():
    l=[1,2,3,3,4]
    count=0
    for i in l:
        f=1
        for j in range(5):
            if i==l[j]:
                f+=1
        if f>2:
            count+=1 
    print(f"no.of dupes {count}")  
dup()                 