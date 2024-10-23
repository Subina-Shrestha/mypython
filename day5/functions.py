#python functions
#a function is a block of cde that performs a specific task
#reusability
#readability
#abstraction,maintainability, testing0
def say_hello():
    print("hello world")
say_hello()#call the function

#passing argument in the functions
def say_hello(name):
    print("hello",name)
say_hello("subina")

#modify the given program to ask a user for a name and call the respective funvtion given by user
def say_hello(name):
    print("hello",name)
names=input("enter a name: ")
say_hello(names)

#wap to ask user to insert two numbers and add those number and display
def sum(a,b):
    c=a+b
    print(f"the sum of a and b is {c}")
x=int(input("enter a number:"))
y=int(input("enter a second number:"))
sum(x,y)

#wap to ask user to insert two numbers and add those number and display(function with argument and return value)
def sum(a,b):
    c=a+b
    return c  
x=int(input("enter a number:"))
y=int(input("enter a second number:"))
z=sum(x,y)
print(f"the sum of {x} and{y}is {z}")

#global scope
name="subina"
def hello_there():
    print(f"the name inside function is{name}")
print(f"the name outside function is {name}")
hello_there()

#to findout the square of numbers
def find_square(num):
    result=num*num
    return result
square=find_square(4)
print(f"the result of square is:{square}")

#function that takes two numbers a and b, calculate a^b
def find_power(a,b):
    result=1
    for i in range(b):
        result=result*a#result=1*2 result=2*2=4 result=4*2=8
    return result
x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=find_power(x,y)
print("the result is: ",z)

#another method
def powerArko(a,b):
    return a**b
x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=find_power(x,y)
print("the result is: ",z)

#wap using functions to calculate the factorial of given number
def fact(num):
    factor=1
    for i in range(1,num+1):
        factor=factor*i
    return factor
number=int(input("enter a number"))
z=fact(number)
print(f"the result is: ",z)

#recursive function
def recursiveFact(num):
    if num==0:
        return 1
    return num*recursiveFact(num-1)

number=int(input("enter a number"))
z=fact(number)
print(f"the result is: ",z)

#wap using recursive function to find the number from 1 to 5
def sumtilln(n):
    if(n==0):
        return 0
    return n+sumtilln(n-1)
number=int(input("enter a number:"))
z=sumtilln(number)
print(f"the sum of the numbers till {number} is ",z)
    
#homework recursion use garerA fiboncacci series patta lagaune




