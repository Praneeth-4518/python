def counts():
    l=['a','e','i','o','u']
    vc=0
    cc=0
    s="hitman"
    for i in s:
        if i in l:
            vc+=1
        else:
            cc+=1
    print(f"no.of vowels and consonents are {vc} and {cc} resp...")    
counts()            