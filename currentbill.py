cno=int(input("enter consumer number :"))
cname=input("enter name :")
pmr=int(input("enter present month reading :"))
lmr=int(input("enter lastmonth reading :"))
tu=pmr-lmr
bill=tu*3.80
print("consumer number:",cno,"\nConsumer name:",cname,"\nPresent month and last month readings are:",pmr,",",lmr,"\nCurrent bill=",bill)