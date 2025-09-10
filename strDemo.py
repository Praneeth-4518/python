def lengthofStr():
    s="Rohit Sharma"
    s2="Hitman"
    count=0
    for i in s:
        count+=1
    print("total no.of chars in",s," are ",count) 
    if s==s2:
        print(f"{s} and {s2} are same")
    else:
        print(f"{s} and {s2} are not same") 
    print("concatenating s2 and s:",end=" ")       
    print(s2+" "+s)    
lengthofStr()       