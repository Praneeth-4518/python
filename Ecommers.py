def eco():
    l=[]
    print("1.ADD PRODUCT/n2.REMOVE PRODUCT/n3.SEARCH PRODUCT/n4.ALL PRODUCT/n5.NO.OF PRODUCTS/n6.SORT/n7.CLEAR/n8.EXIT")
    while(True):
        ch=int(input("enter choice:"))

        if ch==1:
            x=input("enter product to add:")
            l.append(x)
        elif ch==2:
            y=input("enter product to remove:")
            l.remove(y)
        elif ch==3:
            z=input("enter product to search:")
            if z in l:
                print("present")  
        elif ch==4:
            print(l)
        elif ch==5:
            print(len(l)) 
        elif ch==6:
            l.sort() 
        elif ch==7:
            l.clear()
        elif ch==8:
            break        

eco()
          