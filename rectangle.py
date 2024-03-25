from shape import Shape

class Rectangle(Shape):

    def __init__(self, a, b):
        self.check_if_args_not_below_zero(a,b)
        self.a = a
        self.b = b

    def get_area(self):
        area = self.a * self.b
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.a + self.b)
        return perimeter

    def __str__(self):
        return f"Rectangle, a={self.a:0.2f}, b={self.b:0.2f}"

    @classmethod
    def get_area_formula(cls):
        return "a * b"

    @classmethod
    def get_perimeter_formula(cls):
        return "2(a + b)"
