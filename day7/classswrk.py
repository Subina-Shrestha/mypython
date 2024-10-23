#wap to create a clss called person with attributes name and address. inheirit thsi class to another class called student with other parameter added like roll no and semester and facult
#create two student anf print their details
class person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def __str__(self):
        return f"name: {self.name}, address: {self.address}"

class student(person):
    def __init__(self,name,address,rollno,sem,faculty):
        super().__init__(name, address)
        self.rollno=rollno
        self.sem=sem
        self.faculty=faculty
    def __str__(self):
        return f"name:{self.name}, address:{self.address},rollno: {self.rollno} , semester:{self.sem},faculty:{self.faculty}"

p1 = person("Subina", "gkh")
print(p1)
a1=student("subina shrestha","gorkha",39,5,"IT")
print(a1)
        