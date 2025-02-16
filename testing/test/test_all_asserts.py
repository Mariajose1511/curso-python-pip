import unittest
import requests

# URL de la API para obtener las tasas de cambio
API_URL = 'https://api.exchangerate-api.com/v4/latest/US'

# Nombre del servidor
server = 'server a'

def is_api_avaliable():
    # Verificar si la API está disponible
    try:
        response = requests.get(API_URL)
        return response.status_code == 200
    except:
        return False

class AllAssertsTests(unittest.TestCase):
    
    def test_assertEqual_values_are_equal(self):
        # Probar la igualdad de valores
        self.assertEqual(1, 1)
        self.assertEqual('Hola', 'Hola')
    
    def test_assertTrue_or_assertFalse_boolean_values(self):
        # Probar valores booleanos
        self.assertTrue(True)
        self.assertFalse(False)
    
    def test_assertRaises_exception_is_raised(self):
        # Probar que se lanza una excepción
        with self.assertRaises(ValueError):
            int('a')
    
    def test_assertIn_element_is_in_list_or_string(self):
        # Probar si un elemento está en una lista o cadena
        self.assertIn(1, [1, 2, 3])
        self.assertIn('a', 'Hola')
        self.assertNotIn(1, [2, 3, 4])
    
    def test_assertDictEqual_and_assertSetEqual_dicts_and_sets_are_equal(self):
        # Probar la igualdad de diccionarios y conjuntos
        user = {
            'first_name': 'Julio',
            'last_name': 'Ardila'
        }
        self.assertDictEqual({'first_name': 'Julio', 'last_name': 'Ardila'}, user)
        self.assertSetEqual({1, 2, 3}, {3, 2, 1})
    
    @unittest.skip('Trabajo en progreso, se ejecutará posteriormente')
    def test_skip_test_is_skipped(self):
        # Saltar esta prueba
        self.assertEqual(1, 1)
    
    @unittest.skipIf(server == 'server a', 'Saltado porque no estamos en el servidor correcto')
    def test_skipIf_condition_is_true(self):
        # Saltar esta prueba si la condición es verdadera
        self.assertEqual(1, 1)
    
    @unittest.expectedFailure
    def test_expectedFailure_test_is_expected_to_fail(self):
        # Esta prueba se espera que falle
        self.assertEqual(1, 2)
    
    @unittest.skipUnless(is_api_avaliable(), 'API no disponible')
    def test_skipUnless_api_is_available(self):
        # Saltar esta prueba a menos que la API esté disponible
        self.assertTrue(is_api_avaliable())
    
        
