import unittest

# Fonction à tester
def add(a, b):
    return a + b

# Classe de test
class TestAddition(unittest.TestCase):

    def test_addition(self):
        # Appel de la fonction à tester
        result = add(4, 5)

        # Assertion pour vérifier si le résultat est conforme à ce qui est attendu
        self.assertEqual(result, 9, "Le résultat attendu est 9")
        
test_addition = unittest.TestLoader().loadTestsFromTestCase(TestAddition)
unittest.TextTestRunner().run(test_addition)
