def minFreq():
    s="hitmansharma"
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    min=100
    char=''        
    for key in dict:
        if dict[key]<min:
            min=dict[key]
            char=key 
    print("min freq char is ",char, "->",min)
minFreq()