# 

# Progam to calculate perimeter of different polygons and quadrilaterals using inheritance
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A Polygon is a 2D shape with staright lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A trinagle is a polygon with 3 edges")
    Polygon.display_info(self) # passing self explicitly because calling method using class instead of an object
    super.display_info() # acces methods of parent class from inside child class

class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")


t1 = Triangle([5, 6, 7])
prtimeter = t1.get_perimeter()
print(prtimeter)
# method over-riding 
t1.display_info()