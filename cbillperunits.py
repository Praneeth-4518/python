cno=int(input("enter consumer number :"))
cname=input("enter name :")
pmr=int(input("enter present month reading :"))
lmr=int(input("enter lastmonth reading :"))
tu=pmr-lmr
print("total bill:")
if tu<=50:
    print(tu*3.8)
elif tu<=100:
    print((50*3.8)+((tu-50)*4.2))
elif tu<=200:
    print((50*3.8)+((50)*4.2)+(((tu-100)*5.1)))
elif tu<=300:
     print((50*3.8)+((50)*4.2)+((100)*5.1)+((tu-200)*6.3))
else:
    print((50*3.8)+((50)*4.2)+((100)*5.1)+((100)*6.3)+((tu-300)*7.5))              

#print("consumer number:",cno,"\nConsumer name:",cname,"\nPresent month and last month readings are:",pmr,",",lmr,"\nCurrent bill=",bill)