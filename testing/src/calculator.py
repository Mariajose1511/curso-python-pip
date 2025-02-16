def sum(a, b):
    """ 
    Suma dos números.
    
    >>> sum(1, 2)
    3
    >>> sum(5, 5)
    10
    """
    return a + b

def subtract(a, b):
    """ 
    Resta el segundo número del primero.
    
    >>> subtract(5, 2)
    3
    """
    return a - b

def multiply(a, b):
    """ 
    Multiplica dos números.
    
    >>> multiply(5, 2)
    10
    """
    return a * b

def divide(a, b):
    """ 
    Divide el primer número por el segundo.
    
    >>> divide(10, 0)    
    Traceback (most recent call last):
    ZeroDivisionError: Cannot divide by zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
