#wap to display the odd numbers only from 0 to 50
i=0
for i in range(51):
    if i%2!=0:
        print("the odd numbers are ",i)

#wap to check whether the number is prime or not
number= int(input("enter a number:"))
primeflag=False
count=0
for i in range(1,number+1):
    if number%i ==0:
        count=count+1
if count==2:
    print("prime")
else:
    print("composite")
        