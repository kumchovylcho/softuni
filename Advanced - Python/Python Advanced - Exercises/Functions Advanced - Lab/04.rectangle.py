def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return (length * 2) + (width * 2)

    if isinstance(length, int) and isinstance(width, int):
        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    else:
        return "Enter valid values!"

