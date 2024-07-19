import unittest
from mygeolib.shapes import Shape, Circle, Triangle

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(10)
        self.assertAlmostEqual(circle.area(), 314.159265359)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)
        
        triangle = Triangle(5, 7.5, 10)
        self.assertAlmostEqual(triangle.area(), 18.15461, 5)

    def test_right_triangle(self):
        triangle = Triangle(1, 2, 3)
        self.assertFalse(triangle.is_right_triangle())

        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

if __name__ == '__main__':
    unittest.main()

