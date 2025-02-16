def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total

def test_calculate_total_whith_empty_list():
   print('Prueba 1')
   print(calculate_total([]))
   assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    print('Prueba 2')
    products = [
        {'name': 'Product 1',
         'price': 100
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 100

def test_calculate_total_with_multiple_product():
    print('Prueba 3')
    products = [
        {'name': 'Product 1',
         'price': 100,
        },
        {'name': 'Product 2',
         'price': 100,
        },
        {'name': 'Product 3',
         'price': 100,
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 300

if __name__ == '__main__':
    test_calculate_total_whith_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()

