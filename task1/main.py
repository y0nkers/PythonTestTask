from mygeolib import Circle, Triangle, calculate_area

def print_area(shape):
    try:
        area = calculate_area(shape)
        print(f"Площадь фигуры: {area}")
    except TypeError as e:
        print(f"Ошибка вычисления площади: {e}")

def main():
    try:
        circle = Circle(10)
        print_area(circle)

        triangle = Triangle(3, 4, 5)
        print_area(triangle)

        triangle2 = Triangle(1, 2, 3)
        print_area(triangle2)
    except ValueError as e:
        print(f"Ошибка создания фигуры: {e}")

if __name__ == "__main__":
    main()
