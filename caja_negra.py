import unittest

def suma(num_1,num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):
    
    def test_suma_dos_positivos(self):
        num_1 = 25
        num_2 = 44

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado,69)

    def test_suma_dos_negativos(self):
        num_1 = -25
        num_2 = -44

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado,-69)

    def test_suma_psitivo_negativo(self):
        num_1 = -25
        num_2 = 44

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado,19)


if __name__ == '__main__':
    unittest.main(verbosity=2)