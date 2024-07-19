from .shapes import Shape

def calculate_area(shape: Shape):
    if not isinstance(shape, Shape):
        raise TypeError("Объект должен быть экземпляром производного класса Shape!")
    return shape.area()
