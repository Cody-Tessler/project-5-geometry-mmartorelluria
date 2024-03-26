from shape import Shape

class Rectangle(Shape):

    def __init__(self, a, b):
        """
        Constructs a Rectangle object

        :param a: float -> first opposite side of rectangle
        :param b: float -> second opposite side of rectangle
        """
        self.check_if_args_not_below_zero(a,b)
        self.a = a
        self.b = b

    def get_area(self):
        """
        Calculates rectangle area using formula: a * b 

        :return: float -> area of the rectangle
        """
        area = self.a * self.b
        return area

    def get_perimeter(self):
        """
        Calculates perimeter of triangle using formula: 2 * (a + b)

        # :return: float -> perimeter of the rectangle
        """
        perimeter = 2 * (self.a + self.b)
        return perimeter

    def __str__(self):
        return f"Rectangle, a={self.a:0.2f}, b={self.b:0.2f}"

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Rectangle as a string.

        :return: string
        """
        return "a * b"

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Rectangle as a string.

        :return: string
        """
        return "2 * (a + b)"
