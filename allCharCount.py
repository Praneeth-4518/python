def freqs():
    s="hitmansharma"
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else :
            dict[i]=1 
    print(dict) 
    for key in sorted(dict):
        print(key,end="")
        print(dict[key],end=" ")
freqs()              
