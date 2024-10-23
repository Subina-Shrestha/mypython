# #wap to ask user an number and print the prime number in that range
# number= int(input("enter a number:"))

# for i in range(2,number+1):
#         count=0
#         for j in range(1,i+1):
#                 if i%j==0:
#                         count=count+1
#         if count==2:
#             print (j)

# number= int(input("enter a number:"))
# count=0
# while i<=number:
    
#     if number%i ==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("prime")
# else:
#     print("composite")

#converting the second program into while loop
number= int(input("enter a number:"))
i=1
while i<=number:
    count=0
    j=1
    while j<=i:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
        print(i)
    i=i+1
    

        
    