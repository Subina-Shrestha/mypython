#how to extract column from a 2D list
names=["niroj","anish","subina","aayush"]
namewiths=[name for name in names if "s" in name]
print(namewiths)

#code equivalent meaning
#for name in names:
    #if "s" in name:
        #namewiths.append(name)

namewithScapital=[name.upper() for name in names if "s" in name]
print(namewithScapital)

names.sort(reverse=True)
print(names)

#replacement using slicing
thislist=["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3]=["blackcurrant","watermelon"]
print(thislist)

mylist=thislist.copy()#to copy the items from the list
print(mylist)

#make a copy of the list with the list() method i.e using constructor
ohoooo=list(thislist)
print("ohoo=",ohoooo)

#to add two list
list3=ohoooo+mylist
print("list3=",list3)

#using extend() and append()
#extend le entire block of list lai nai ekai patak ligcha append le yeauta yeauta element lai ligcha
list1=[1,2,3]
list2=["a","b","c"]
list1.extend(list2)
print(list1)

#accessing through the index and creating a tuple
tuple=("python","tuple","ordered")
print(tuple[0])

#printing elements using negative indexing
tuple=("python","tuple","ordered")#yesma chai last ko index -1 huncha
print("element at -1 index:",tuple[-1])
print("element between -4 and -1 are: ",tuple[-4:-1])
#set maa chai repeatance hundaina



