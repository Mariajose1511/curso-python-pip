import unittest, os
from datetime import datetime
from unittest.mock import patch
from src.exception import WithdawalTimeRestrictionError,InsuficientFundsError,WithdrawWeekendRestrictionError # importar las excepciones personalizadas
from src.bank_account import BankAccount # importar la clase BankAccount a ser testeada


class BankAccountTests(unittest.TestCase):
    def setUp(self):
        # Configurar una cuenta bancaria con un saldo inicial de 1000
        self.account = BankAccount(balance=1000, log_file='transaction_log.txt')
    
    def tearDown(self):
       if os.path.exists(self.account.log_file):
          os.remove(self.account.log_file)
    
    def count_lines(self):
        with open(self.account.log_file, 'r') as file:
            return len(file.readlines())

    def test_deposit_positive_amount_increases_balance(self):
        # Probar la función de depósito
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, 'El balance no es igual')
    
    @patch('src.bank_account.datetime')
    def test_withdraw_positive_amount_decreases_balance(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        # Probar la función de retiro
        new_balance = self.account.withdraw(500)
        self.assertEqual(new_balance, 500, 'El balance no es igual')
    
    def test_get_balance_initial_balance_is_correct(self):
        # Probar la función de obtener saldo
        self.assertEqual(self.account.get_balance(), 1000, 'El balance no es igual')
    
    def test_transfer_positive_amount_decreases_balance(self):
        # Probar la función de transferencia
        new_balance = self.account.transfer(1000)
        self.assertEqual(self.account.get_balance(), 0, 'Fondos insuficientes')
    
    def test_transfer_insufficient_funds_raises_error(self):
        # Probar la transferencia con fondos insuficientes
        with self.assertRaises(ValueError):
            self.account.transfer(1001)
    
    def test_transaction_log_file_created_after_deposit(self):
        # Probar que el archivo de registro de transacciones se crea después de un depósito
        self.account.deposit(500)
        self.assertTrue(os.path.exists('transaction_log.txt'))
    
    def test_count_transaction_lines_increases_after_deposit(self):
        # Probar que el número de líneas en el archivo de registro de transacciones es correcto
        self.assertEqual(self.count_lines(), 1)
        self.account.deposit(500)
        self.assertEqual(self.count_lines(), 2)
    
    def test_transfer_log_no_new_entry_on_insufficient_funds(self):
        # Probar que no se añade una nueva entrada en el registro de transacciones si los fondos son insuficientes
        with self.assertRaises(ValueError):
            self.account.transfer(5000)
        self.assertEqual(self.count_lines(), 2)
        
    @patch('src.bank_account.datetime')
    def test_withdraw_outside_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 9
        new_balance = self.account.withdraw(500)
        self.assertEqual(new_balance, 500, 'El balance no es igual')
    
    @patch('src.bank_account.datetime')
    def test_withdraw_disallow_before_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdawalTimeRestrictionError):
            self.account.withdraw(500)
            
    @patch('src.bank_account.datetime')
    def test_withdraw_disallow_after_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 20
        with self.assertRaises(WithdawalTimeRestrictionError):
            self.account.withdraw(500)
    
    @patch('src.bank_account.datetime')        
    def test_witdraw_disallow_weekend(self,mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 2, 3, 10, 0, 0)  # Sábado 3 de febrero 2024        
        with self.assertRaises(WithdrawWeekendRestrictionError):
            self.account.withdraw(500)
            
    def test_deposit_multiple_amount(self):
        test_cases =[
            {'amount':500, 'expected':1500},
            {'amount':1000, 'expected':2000},
            {'amount':2000, 'expected':3000}
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file='transaction_log.txt')
                new_balance = self.account.deposit(case['amount'])
                self.assertEqual(new_balance, case['expected'], 'El balance no es igual')