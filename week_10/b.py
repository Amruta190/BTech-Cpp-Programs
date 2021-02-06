class Circle():
    def _init_(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14
rad=int(input("Enter radius of circle : "))
NewCircle=Circle(rad)
print(f"Area of circle is {NewCircle.area()}")
print(f"Perimeter of circle is {NewCircle.perimeter()}")