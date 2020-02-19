import unittest
from lib import *


class TestStringMethods(unittest.TestCase):

    def testsuma(self):
        a = (2, 3)
        b = (3, 1)
        self.assertEqual(suma(a, b), (5, 4))

    def testresta(self):
        a = (2, 3)
        b = (3, 1)
        self.assertEqual(resta(a, b), (-1, 2))

    def testmulti(self):
        a = (2, 3)
        b = (3, 1)
        self.assertEqual(multi(a, b), (3, 11))

    def testdivisi(self):
        a = (2, 3)
        b = (3, 1)
        self.assertEqual(division(a, b), (0.9, 0.7))

    def testconjugado(self):
        a = (2, 3)
        self.assertEqual(conjugado(a), (2, -3))

    def testmodulos(self):
        a = (2, 3)
        self.assertEqual(modulos(a), (3.61, 0))

    def testcartesianos(self):
        a = (2, 3)
        self.assertEqual(cartesiapolar(a), (3.61, 0.59))

    def testretorno(self):
        a = (2, 3)
        self.assertEqual(retorno(a), (0.98, 0))

    def testsumavector(self):
        a = [(1,6),(5,7)]
        b = [(1,5),(7,2)]
        self.assertEqual(sumavector(a, b), [(2, 11), (12, 9)])

    def testmultiescalar(self):
        a = [(1,5),(7,2)]
        b = (5,0)
        self.assertEqual(multiescalar(a, b), [(5, 25), (35, 10)])

    def testsumamatriz(self):
        a = [(5,2),(3,8)], [(1,5),(7,7)]
        b = [(1,9),(2,2)], [(3,1),(9,2)]
        self.assertEqual(sumaMatriz(a, b), [[(6, 11), (5, 10)], [(4, 6), (16, 9)]])

    def testinversamatriz(self):
        a = [(5,2),(3,8)], [(1,5),(7,7)]
        self.assertEqual(inversaMatriz(a), [[(-5, -2), (-3, -8)], [(-1, -5), (-7, -7)]])

    def testescalarmatriz(self):
        a = [(5,2),(3,8)], [(1,5),(7,7)]
        b = (5,0)
        self.assertEqual(escalarmatrices(a, b), [[(25, 10), (15, 40)], [(5, 25), (35, 35)]])

    def testtranspuesta(self):
        a = [(5,2),(3,8)], [(1,5),(7,7)]
        self.assertEqual(transpuesta(a), [[(5, 2), (1, 5)], [(3, 8), (7, 7)]])

    def testconjugadomatriz(self):
        a = [(5,2),(3,8)], [(1,5),(7,7)]
        self.assertEqual(conjumatrices(a),[[(5, -2), (3, -8)], [(1, -5), (7, -7)]])

    def testadjuntamatriz(self):
        a =  [(5,2),(3,8)], [(1,5),(7,7)]
        self.assertEqual(adjunmatrices(a), [[(5, -2), (1, -5)], [(3, -8), (7, -7)]])

    def testmultimatrices(self):
        a = [(5,2),(3,8)], [(1,5),(7,7)]
        b = [(1,9),(2,2)], [(3,1),(9,2)]
        self.assertEqual(multimatriz(a, b), [(-13, 47), (-10, 22), (13, 11), (11, 78), (-44, 14), (0, 28), (-2, 16), (49, 77)])

    def testaccion(self):
        a = [(5,2),(3,8)], [(1,5),(7,7)]
        b = [(1,5),(7,2)]
        self.assertEqual(accionmatvector(a, b), [(5, 62), (35, 63)])

    def testinterno(self):
        a = [(1,5),(7,2)]
        b =  [(1,6),(5,7)]
        self.assertEqual(interno(a, b), (49, 39))

    def testnorma(self):
        a = [(1,5),(7,2)]
        self.assertEqual(norma(a), 7.28)
