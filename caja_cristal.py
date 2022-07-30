import unittest

def mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    def test_mayor_de_edad(self):
        edad = 20
        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, True)
    
    def test_menor_de_edad(self):
        edad = 17
        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, False)  #assert.Equal compara los dos resultados para ver si 
                                            #tenemos el esperado.

if __name__ == '__main__':
    unittest.main(verbosity=2)