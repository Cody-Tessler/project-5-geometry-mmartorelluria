from shape import Shape
import math

class Circle(Shape):

    def __init__(self, r):
        """
        Constructs a Circle object 

        :param a: float -> radius of circle
        """
        self.check_if_args_not_below_zero(r)
        self.r = r
    
    def get_area(self):
        """
        Calculates circle area using formula: {math.pi} * r ** 2

        :return: float -> area of the circle
        """
        area = math.pi * self.r ** 2
        return area

    def get_perimeter(self):
        """
        Calculates perimeter of circle using formula: 2 * {math.pi} * r

        :return: float -> perimeter of the circle
        """
        perimeter = 2 * math.pi * self.r
        return perimeter

    def __str__(self):
        return f"Circle, r={self.r:0.2f}"

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Circle as a string.

        :return: string
        """
        return f"{math.pi} * r ** 2"

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Circle as a string.

        :return: string
        """
        return f"2 * {math.pi} * r"
