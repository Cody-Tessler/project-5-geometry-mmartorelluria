from shape import Shape
import math

class Circle(Shape):

    def __init__(self, r):
        self.check_if_args_not_below_zero(r)
        self.r = r
    
    def get_area(self):
        area = math.pi * self.r ** 2
        return area

    def get_perimeter(self):
        perimeter = 2 * math.pi * self.r
        return perimeter

    def __str__(self):
        return f"Circle, r={self.r:0.2f}"

    @classmethod
    def get_area_formula(cls):
        return f"{math.pi} * r ** 2"

    @classmethod
    def get_perimeter_formula(cls):
        return f"2 * {math.pi} * r"
