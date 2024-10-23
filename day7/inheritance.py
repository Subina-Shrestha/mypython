#inheritance ko lagi is a relationship hunai parcha
class shape:
    def __init__(self,side,side2):
        self.side=side
        self.side2=side2
    def getArea(self):
        return self.side*self.side2
    def __str__(self):#str returns string
        return f"the area of the given {self.__class__.__name__}is {self.getArea()}"
    

class rectangle(shape):
    def __init__(self,side, side2):
        super().__init__(side,side2)

class triangle(shape):
    def __init__(self,side):
        super().__init__(base,height)
        #method overriding
    def get_area(self):
        area=super().get_area()
        return area/2

class square(rectangle):
    def __init__(self,side):
        super().__init__(side,side)

triangle=shape(3,4)
print(triangle)

square=shape(5,5)
print(square)