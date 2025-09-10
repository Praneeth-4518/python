def freq(l,ele):
    
    f=0
    for i in l:
        if i==ele:
            f+=1
    print(f"freq of {ele} in list is {f}")
l=[45,18,93,45,18,45]
ele=45     
freq(l,ele)    