import unittest  # Importar el módulo unittest para crear y ejecutar pruebas
import os  # Importar os para operaciones del sistema de archivos
from faker import Faker  # Importar Faker para generar datos falsos
from src.user import User  # Importar la clase User desde el módulo user
from src.bank_account import BankAccount  # Importar la clase BankAccount desde el módulo bank_account

class UserTest(unittest.TestCase):
    # Definir una clase de prueba que hereda de unittest.TestCase

    def setUp(self):
        # Configurar el entorno de prueba
        self.faker = Faker(locale='es_ES')  # Crear una instancia de Faker con localización en español
        self.user = User(name=self.faker.name(), email=self.faker.email())  # Crear un usuario con datos falsos

    def test_user_creation(self):
        # Probar la creación de un usuario
        name_generate = self.user.name  # Obtener el nombre generado para el usuario
        email_generate = self.user.email  # Obtener el correo electrónico generado para el usuario
        self.assertEqual(self.user.name, name_generate)  # Verificar que el nombre del usuario es el esperado
        self.assertEqual(self.user.email, email_generate)  # Verificar que el correo electrónico del usuario es el esperado

    def test_user_with_multiply_accounts(self):
        # Probar que un usuario puede tener múltiples cuentas bancarias
        for _ in range(5):
            # Crear y añadir 5 cuentas bancarias al usuario
            bank_account = BankAccount(
                balance=self.faker.random_int(min=1000, max=5000),  # Generar un saldo aleatorio
                log_file=self.faker.file_name(extension='txt')  # Generar un nombre de archivo de registro
            )
            self.user.add_account(account=bank_account)  # Añadir la cuenta bancaria al usuario

        expected_value = self.user.get_total_balance()  # Obtener el saldo total esperado del usuario
        value = sum(account.get_balance() for account in self.user.accounts)  # Calcular el saldo total sumando los saldos de todas las cuentas
        self.assertEqual(expected_value, value)  # Verificar que el saldo total es el esperado

    def tearDown(self):
        # Limpiar el entorno de prueba
        for account in self.user.accounts:
            os.remove(account.log_file)  # Eliminar los archivos de registro de las cuentas bancarias