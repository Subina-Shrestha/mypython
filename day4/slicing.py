#kunai pani list ko subset lai slice vaninxa
#list_name[start:end:step]
#start: starting index
#end: ending index
mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist)
newlist=mylist[1:5]#mathillo range chai exxclude huncha tallo range include
print(newlist)
newlist1=mylist[:4]
print(newlist1)
newlist2=mylist[7:]
print(newlist2)

#to insert a new value in the list
nayalist=["subina","kritima","anish"]
nayalist.insert(1,"sushil")
print(nayalist)

#to replace a new value and remove
nayalist.remove("subina")
nayalist.append("sushila")

#classwork
sentence="the quick brown fox jumps over the lazy dog"
word=sentence[35:39]
print(word)

#how to filter a list
mylist=[]
for i in range(21):
    mylist.append(i)
print(mylist)
multiple=mylist[5::5]
print(multiple)

#insert le chai particular index maa insert garcha, tara append le chai last maa add garcha list ko 
#list maa duplicate value cha bhane remove le first occurence lai remove garcha 
#del listname[2] ani pop()le chai particular vlaue remove garcha
#del listname le chai entire list lai nai remove garcha
#thislist.clear() le chai truncate jastai kaam garcha

