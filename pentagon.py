from shape import Shape
import math

class Pentagon(Shape):

    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a

    def get_area(self):
        area = (1 / 4) * math.sqrt(5(5+2*math.sqrt(5))) * self.a ** 2
        return area

    def get_perimeter(self):
        perimeter = 5 * self.a
        return perimeter

    def __str__(self):
        return f"Pentagon, a={self.a:0.2f},"

    @classmethod
    def get_area_formula(cls):
        return "(1/4) * sqrt(5(5+2sqrt(5))) * a**2"

    @classmethod
    def get_perimeter_formula(cls):
        return "5a"
