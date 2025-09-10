def maxFreq():
    s="hitmansharma"
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    max=0
    char=''        
    for key in dict:
        if dict[key]>max:
            max=dict[key]
            char=key 
    print("max freq char is ",char, "->",max)
maxFreq()                       