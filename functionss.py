#fuction that helps
#len()
ml=[1,15,9,2,6,3,5]
print("original list:",ml)
ml.append(4)
print("after adding 4 the list: ",ml)
ml.sort()
#sorting ko lagi datatype same hunu paryo
print("after sorting in ascending:",ml)
ml.sort(reverse= True)
print("after sorting in descending:",ml)
print(ml)
print("the number 15 appears: ",ml.count(15),"times")
ml.remove(2)
print("after removal of 2, the list is: ",ml)


#tuple=tuple imutable ho ysma append garna mildaina
tuples=[1,2,3]
print(tuples)
# tuples.append['hello']
# print(tuples)
itemcounts=len(tuples)
largestitem=max(tuples)
smallestitem=min(tuples)
sumofallitems=sum(tuples)
