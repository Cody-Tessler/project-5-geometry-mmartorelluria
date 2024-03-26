from shape import Shape
import math

class Pentagon(Shape):

    def __init__(self, a):
        """
        Constructs a Pentagon object

        :param a: float -> sides of pentagon
        """
        self.check_if_args_not_below_zero(a)
        self.a = a

    def get_area(self):
        """
        Calculates pentagon area using formula: (1/4) * sqrt(5(5+2sqrt(5))) * a**2

        :return: float -> area of the pentagon
        """
        area = (1/4) * (math.sqrt(5*(5+2*(math.sqrt(5))))) * self.a ** 2
        # area = "{:.2f}".format(area) # https://python.shiksha/tips/limiting-float-upto-2-places/
        return area

    def get_perimeter(self):
        """
        Calculates perimeter of pentagon using formula: 5 * a

        :return: float -> perimeter of the pentagon
        """
        perimeter = 5 * self.a
        return perimeter

    def __str__(self):
        return f"Pentagon, a={self.a:0.2f},"

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Pentagon as a string.

        :return: string
        """
        return "(1/4) * sqrt(5(5+2sqrt(5))) * a**2"

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Pentagon as a string.

        :return: string
        """
        return "5 * a"
