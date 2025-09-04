sno=int(input("enter student number :"))
sname=input("enter name :")
m=int(input("enter math marks :"))
p=int(input("enter phy marks :"))
c=int(input("enter che marks :"))

if m>=40 and p>=40 and c>=40:
    avg=(m+p+c)/3
    if avg>80:
        print("grade:distension")
    elif avg>70:
        print("grade:A")
    elif avg>50:
        print("grade:B")
    else:
        print("grade:C")            
else:
    print("Fail")
#print("student number:",sno,"\nStudent name:",sname,"\nmarks in math,phy,che are:",m,",",p,",",c,"\naverage marks=",round(avg,2))