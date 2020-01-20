import unittest
from lib import *

class TestStringMethods(unittest.TestCase):

    def testsuma(self):
        a = (2,3)
        b = (3,1)
        self.assertEqual(suma (a,b), (5,4))
    def testresta(self):
        c = (2,3)
        d = (3,1)
        self.assertEqual(resta (c,d), (-1,2))
    def testmulti(self):
        e = (2,3)
        f = (3,1)
        self.assertEqual(multi (e,f), (3,11))
    def testdivisi(self):
        g = (2,3)
        h = (3,1)
        self.assertEqual(division (g,h), (0.9,0.7))
    def testconjugado(self):
        i = (2,3)
        self.assertEqual(conjugado (i), (2,-3))
    def testmodulos(self):
        j = (2,3)
        self.assertEqual(modulos (j), (3.61,0))
    def testcartesianos(self):
        k = (2,3)
        self.assertEqual(cartesiapolar (k), (3.61,0.98))
    def testretorno(self):
        l = (2,3)
        self.assertEqual(retorno (l), (0.98,0))


        
if __name__ == '__main__':
    unittest.main()
