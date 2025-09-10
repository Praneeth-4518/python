def dictDemo():
    dict={1:"GOT",2:"HOTD",3:"VIKINGS"}
    dict[4]="CURSED"
    print(dict)
    dict.pop(4)
    print(dict)
    ch=int(input("enter key to search:"))
    if ch in dict:
        print(dict[ch])
    ch=int(input("enter id to update value:"))
    val=input("enter value to be update:")
    if ch in dict:
        dict[ch]=val
    print(dict) 
    count=0      
    for i in dict.values():
        print(i,end=" ") 
        count+=1
    print("\ntotal books are ",count)
    vall=input("enter  value to check:") 
    if vall in dict.values():
        print("present")
    else:
        print("not present")          
dictDemo()   