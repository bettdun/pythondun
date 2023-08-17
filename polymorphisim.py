# polymorphisim allow different objects to respond to same classmethod
# ii there on way


class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        def area (self):
            return 3.14*self.radius *+2
class square:
    def __init__(self,side):
        self.side=side
        def area(self):
            return  self.side *+2
# creating objects
shape= (circle(5).square(4)):

for i in  shape:
    print("area:", i.area())
