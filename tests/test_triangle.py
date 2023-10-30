import pytest
import unittest
from triangle import triangle

# Unit testing using classes

class testingTriangle(unittest.TestCase):

    def test_equilateral_triangle(self):
        assert triangle(3, 3, 3) == "Equilateral"

    def test_isosceles_triangle(self):
        assert triangle(3, 3, 2) == "Isoscalene"
        assert triangle(3, 2, 3) == "Isoscalene"
        assert triangle(2, 3, 3) == "Isoscalene"

    def test_scalene_triangle(self):
        assert triangle(3, 4, 5) == "Scalene"

    def test_invalid_inputs(self):
        assert triangle(0, 3, 3) == "Error, values must be >0"
        assert triangle(3, 0, 3) == "Error, values must be >0"
        assert triangle(3, 3, 0) == "Error, values must be >0"
        assert triangle(3, 3, "3") == "Not integer"
        assert triangle("3", 3, 3) == "Not integer"
        assert triangle(3, "3", 3) == "Not integer"
