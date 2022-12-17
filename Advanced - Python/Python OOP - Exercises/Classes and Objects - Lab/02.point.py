class Point:

    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"
