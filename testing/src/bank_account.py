
from datetime import datetime
from src.exception import WithdawalTimeRestrictionError,InsuficientFundsError,WithdrawWeekendRestrictionError

class BankAccount:
    def __init__(self, balance,log_file=None):
        # Inicializar la cuenta bancaria con un saldo inicial
        self.balance = balance
        self.log_file = log_file
        self._log_transaction(f'Cuenta creada con un saldo de {balance}')
    
    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as file:
                file.write(f'{message}\n')

    def deposit(self, positive_amount):
        # Depositar una cantidad en la cuenta si es mayor que 0
        """ 
        >>> account = BankAccount(1000)
        >>> account.deposit(500)
        1500
        """
        if positive_amount > 0:
            self.balance += positive_amount
            self._log_transaction(f'Depósito de {positive_amount}. Saldo actual: {self.balance}')
        return self.balance
    
    def withdraw(self, positive_amount):
        
        now = datetime.now() 
        """ 
        >>> account = BankAccount(1000)
        Traceback (most recent call last):
        WithdawalTimeRestrictionError: No se puede retirar dinero fuera del horario de oficina
        
        """       
        if now.hour < 9 or now.hour > 17:
            raise WithdawalTimeRestrictionError('No se puede retirar dinero fuera del horario de oficina')
        
        '''
        >>> account = BankAccount(1000)
        Traceback (most recent call last):
        WithdrawWeekendRestrictionError: No se puede retirar dinero los fines de semana
        '''
        if now.weekday() in [5, 6]:        
            raise WithdrawWeekendRestrictionError('No se puede retirar dinero los fines de semana')
        # Retirar una cantidad de la cuenta si es mayor que 0 y menor o igual al saldo
        """ 
        >>> account = BankAccount(1000)
        >>> account.withdraw(500)
        500
        """
        if positive_amount > 0 and positive_amount <= self.balance:
            self.balance -= positive_amount
            self._log_transaction(f'Retiro de {positive_amount}. Saldo actual: {self.balance}')
        return self.balance
    
    def get_balance(self):
        # Obtener el saldo actual de la cuenta
        """ 
        >>> account = BankAccount(1000)
        >>> account.get_balance()
        1000
        """
        self._log_transaction(f'Saldo actual: {self.balance}')
        return self.balance
    
    def transfer(self, positive_amount):
        # Transferir una cantidad de la cuenta si es mayor que 0 y menor o igual al saldo
        """ 
        >>> account = BankAccount(4000)
        >>> account.transfer(2000)
        2000
        """
        if positive_amount > 0 and positive_amount <= self.balance:
            self.balance -= positive_amount
            self._log_transaction(f'Transferencia de {positive_amount}. Saldo actual: {self.balance}')
        else:
            self._log_transaction(f'Transferencia fallida. Saldo insuficiente')
            raise ValueError('Saldo insuficiente')            
        return self.balance