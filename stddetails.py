sno=int(input("enter student number"))
sname=input("enter name")
m=int(input("enter math marks"))
p=int(input("enter phy marks"))
c=int(input("enter che marks"))
avg=(m+p+c)/3
print("student number:",sno,"\nStudent name:",sname,"\nmarks in math,phy,che are:",m,",",p,",",c,"\naverage marks=",round(avg,2))