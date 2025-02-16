import unittest  # Importar el módulo unittest para crear y ejecutar pruebas
from test_banck_account import BankAccountTests  # Importar la clase de pruebas BankAccountTests
from test_calculator import CalculatorTests  # Importar la clase de pruebas CalculatorTests

def bank_account_suite():
    # Crear una suite de pruebas para BankAccountTests
    suite = unittest.TestSuite()
    # Añadir la prueba test_deposit a la suite
    suite.addTest(BankAccountTests('test_deposit_positive_amount_increases_balance'))
    # Añadir la prueba test_withdraw a la suite
    suite.addTest(BankAccountTests('test_withdraw_positive_amount_decreases_balance'))
    return suite  # Devolver la suite de pruebas

def calculator_suite():
    # Crear una suite de pruebas para CalculatorTests
    suite = unittest.TestSuite()
    # Añadir la prueba test_sum a la suite
    suite.addTest(CalculatorTests('test_sum_two_numbers_returns_correct_result'))
    # Añadir la prueba test_subtract a la suite
    suite.addTest(CalculatorTests('test_subtract_two_numbers_returns_correct_result'))
    return suite  # Devolver la suite de pruebas

if __name__ == '__main__':
    # Crear un ejecutor de pruebas
    runner = unittest.TextTestRunner()
    # Ejecutar la suite de pruebas para CalculatorTests
    runner.run(calculator_suite())
    # Ejecutar la suite de pruebas para BankAccountTests
    runner.run(bank_account_suite())