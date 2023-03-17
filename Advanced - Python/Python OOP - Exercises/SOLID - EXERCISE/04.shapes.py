from abc import abstractmethod, ABC
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height / 2


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


class AreaCalculator:

    def __init__(self, shapes: list):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("`shapes` should be of type `list`.")

        self.__shapes = value

    @property
    def total_area(self):
        return sum(shape.calculate_area() for shape in self.shapes)


all_shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(5)]
calculator = AreaCalculator(all_shapes)
print("The total area is: ", calculator.total_area)
