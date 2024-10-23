#fuction that helps
#len()
ml=['s','v','a','n','subina','.','/']
#lexographical le . / haru sabai lai arrange garcha
print("original list:",ml)
ml.append('r')
print("after adding 4 the list: ",ml)
ml.sort()
#sorting ko lagi datatype same hunu paryo
print("after sorting in ascending:",ml)
ml.sort(reverse= True)
print("after sorting in descending:",ml)
print(ml)
# print("the number 15 appears: ",ml.count(15),"times")
# ml.remove(2)
# printf("after removal of 2, the list is: ",ml)