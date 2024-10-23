#default argument
def add_number(a=7,b=8):
    sum=a+b
    print("sum: ",sum)
add_number(2,3)

#function with one argument
add_number(a=2)
add_number()

#example
def displayInfo(firstname,lastname):
    print("first name: ",firstname)
    print("last name: ",lastname)
displayInfo(firstname="subina", lastname="shrestha")#special python function

#program to find sum of multiple numbers
def find_sum(*numbers):#ysma* le number of argument pack gariyeko bhanne bujhaucha
    result=0
    for num in numbers:
        result=result+num
    print("sum= ",result)
#function call with 3 arguments
find_sum(1,2,3)
#function call with 2 arguments
find_sum(4,9)

#wap in python to ask a user to enter a number until the user enters zero now create a function that pass this number and find the max among them and return it.
#your program should print the maximum number
mynums=[]
while True:
    x=int(input("enter a number:"))
    if(x==0):
        break
    mynums.append(x)
def find_max(numbers):
    max=0
    for n in numbers:
        if n>max:
            max=n
    return max
maximum=find_max(mynums)
print(f"the maximum number is {maximum}")

#another method
import sys
mynums=[]
while True:
    x=int(input("enter a number:"))
    if(x==0):
        break
    mynums.append(x)        
def findminmax(numbers):
    max=0
    min=sys.maxsize
    for n in numbers:
        if n>max:
            max=n
        if n<min:
            min=n
    return [max,min]
maximum,minimum=findminmax(mynums)


