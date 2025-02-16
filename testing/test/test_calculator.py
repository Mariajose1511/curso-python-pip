import unittest # importar el módulo unittest
from src.calculator import sum,subtract,multiply,divide # importar las funciones a ser testeadas

class CalculatorTests(unittest.TestCase):
    
    def test_sum_two_numbers_returns_correct_result(self):
        # Probar la función de suma
        assert sum(1, 2) == 3
    
    def test_subtract_two_numbers_returns_correct_result(self):
        # Probar la función de resta
        assert subtract(2, 1) == 1
    
    def test_multiply_two_numbers_returns_correct_result(self):
        # Probar la función de multiplicación
        assert multiply(2, 2) == 4
    
    def test_divide_two_numbers_returns_correct_result(self):
        # Probar la función de división
        assert divide(4, 2) == 2
    
    def test_divide_by_zero_raises_zero_division_error(self):
        # Probar la división por cero
        with self.assertRaises(ZeroDivisionError):
            divide(4, 0)


    