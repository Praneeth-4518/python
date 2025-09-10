def counts():
    s="Hitman@45"
    cc=0
    dc=0
    sc=0
    for i in s:
        if (i>=chr(65) and i<=chr(91)) or (i>=chr(97) and i<=chr(123)):
            cc+=1
        elif i>='0' and i<='9':
            dc+=1
        else:
            sc+=1
    print(f"no of chars,digits,special chars in {s} are {cc} ,{dc} ,{sc} respectively") 
counts()                   