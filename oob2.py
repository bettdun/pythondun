class circles:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius  ** 2
circles=circles(7)
print("my circles area is",circles.area() )