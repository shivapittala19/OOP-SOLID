import math

class Triangle:
    def __init__(self) -> None:
        self.points = []
    
    def add_points(self,point):
        self.points.append(point)
        
    def length_of_side(self,point1,point2):
        x1, y1 = point1
        x2, y2 = point2
        
        return round(math.sqrt((x2-x1)**2 + (y2-y1)**2),3)
    
    def perimeter(self):
        if len(self.points) < 3:
             print("Not a triangle,It require atlest 3 points")
             return 
        
        point1, point2, point3 = self.points
        
        side1 = self.length_of_side(point1,point2)
        side2 = self.length_of_side(point2,point3)
        side3 = self.length_of_side(point3,point1)
        
        if side1 + side2 <= side3 or side2 + side3 <= side1 or side3 + side1 <= side2:
            print("These points do not form a Triangle")
            return 0
        return side1 + side2 + side3
    
    def is_equal(self,another_triangle):
        for point in self.points:
            if point not in another_triangle.points:
                return False
        return True
        
    
t1 = Triangle()
t1.add_points((0,1))
t1.add_points((6,0))
t1.add_points((0,4))
print(t1.perimeter())

t2 = Triangle()
t2.add_points((0,1))
t2.add_points((6,0))
t2.add_points((0,4))
print(t2.is_equal(t1))

t3 = Triangle()
t3.add_points((0,1))
t3.add_points((9,0))
t3.add_points((5,4))
print(t3.is_equal(t1))