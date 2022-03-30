# Create a class Triangle and initialize it with height and base and create a method area to return the area of the triangle.
class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def Area(self):
        ans = (self.height * self.base)/ 2
        return ans
triangle1 = Triangle(4, 5)
print(triangle1.Area())
