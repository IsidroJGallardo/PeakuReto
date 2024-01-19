import unittest
from main import sumar_n_elementos_segunda_columna

class TestSumarNElementosSegundaColumna(unittest.TestCase):

    def test_suma_correcta(self):
        datos_departamentos = {
            'Administration': 200,
            'Marketing': 201,
            'Purchasing': 114,
            'Human Resources': 203,
            'Shipping': 121,
            'IT': 103,
            'Public Relations': 204,
            'Sales': 145,
            'Executive': 100
        }

        # Verificar que la suma de los primeros 3 elementos es 515
        resultado = sumar_n_elementos_segunda_columna(datos_departamentos, 3)
        self.assertEqual(resultado, 515)

    def test_suma_cero_elementos(self):
        datos_departamentos = {
            'Administration': 200,
            'Marketing': 201,
            'Purchasing': 114
        }

        # Verificar que la suma de cero elementos es cero
        resultado = sumar_n_elementos_segunda_columna(datos_departamentos, 0)
        self.assertEqual(resultado, 0)

    def test_suma_cantidad_mayor_a_datos(self):
        datos_departamentos = {
            'Administration': 200,
            'Marketing': 201
        }

        # Verificar que la suma de más elementos de los disponibles es la suma de todos los elementos
        resultado = sumar_n_elementos_segunda_columna(datos_departamentos, 5)
        self.assertEqual(resultado, 401)

if __name__ == '__main__':
    unittest.main()