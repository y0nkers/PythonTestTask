import unittest
from mygeolib.shapes import Circle, Triangle
from mygeolib.calculate_area import calculate_area

class TestAreaCalculator(unittest.TestCase):
    def test_calculate_circle_area(self):
        circle = Circle(10)
        self.assertAlmostEqual(calculate_area(circle), 314.15927, 5)

    def test_calculate_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(calculate_area(triangle), 6)
        
        triangle = Triangle(5, 7.5, 10)
        self.assertAlmostEqual(calculate_area(triangle), 18.15461, 5)

    def test_invalid_shape(self):
        with self.assertRaises(TypeError):
            calculate_area(1)
        
        with self.assertRaises(TypeError):
            calculate_area("Треугольник")

if __name__ == '__main__':
    unittest.main()
