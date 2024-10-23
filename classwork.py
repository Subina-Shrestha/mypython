# #wap to ask the user to enter a number anf tell if the number is odd or even
# # #yesma if bhitra khali rakhna paidaina
# number=int(input("enter a number"))
# if number%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")

# # #wap to ask the user to enter her age an decide if she is elligible for voting or not
# age=int(input("enter your age:"))

# if(age>=18):
#     print("you are eligible for vitong")
# else:
#     print("you are not eligible")

#wap to ask a user marks obtained in 5 subjects an calculate the percentage. displayy division
m1=float(input("enter the 1st marks"))
m2=float(input("enter the 2nd marks"))
m3=float(input("enter the 3rd marks"))
m4=float(input("enter the 4th marks"))
m5=float(input("enter the 5h marks"))
sum=m1+m2+m3+m4+m5
percen=sum*100/500
if percen>=80:
    print("distinction")
if percen<80 and percen>=60:
    print("first dividion",percen)
if percen<60 and percen>=50:
    print("second dividion",percen)
if percen<50 and percen>=32:
    print("third dividion",percen)
else:
    print("fail",percen)