#set  operations
myset={'ram','hari','sita','gita','male'}
set1={'abc',34,True,40,'male'}
#object code ko lagi python -m dis filename.py

set3=set1.union(myset)
print(set3)

set4=set1.intersection(myset)
print("the intersection operations is: ",set4)

set5=set1.difference(myset)
#difference le intersectiion ko complement dincha
print("the difference operations is: ",set5)