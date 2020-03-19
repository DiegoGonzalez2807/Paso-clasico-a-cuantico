import unittest
from Clasico_a_cuantico import *
class TestStringMethods(unittest.TestCase):
    def test_canica(self):
        a = [[(0,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
             [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
             [(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],
             [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
             [(0,0),(0,0),(1,0),(0,0),(0,0),(1,0)],
             [(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)]]
        estado = [(8,0),(1,0),(9,0),(5,0),(4,0),(2,0)]
        click = 3
        self.assertEqual(experimento_canica(a,estado,click), [(15, 0), (5, 0), (20, 0), (5, 0), (32, 0), (26, 0)])
    def test_potencia(self):
        a = [[(0,0),(0,0),(1/9,0),(1/27,0),(5/4,0),(10/3,0)],
             [(0,0),(0,0),(1/9,0),(5/9,0),(5/9,0),(5/18,0)],
             [(1/9,0),(2/9,0),(1/6,0),(1/3,0),(1/18,0),(1/9,0)],
             [(2/9,0),(1/9,0),(1/3,0),(1/6,0),(1/9,0),(1/18,0)],
             [(2/9,0),(4/9,0),(1/9,0),(3/5,0),(0,0),(0,0)],[(4/9,0),(2/9,0),(2/9,0),(1/9,0),(0,0),(0,0)]]
        click=1
        self.assertEqual(potencia (a,click), [[(0, 0), (0, 0), (0.1111111111111111, 0), (0.037037037037037035, 0), (1.25, 0), (3.3333333333333335, 0)], [(0, 0), (0, 0), (0.1111111111111111, 0), (0.5555555555555556, 0), (0.5555555555555556, 0), (0.2777777777777778, 0)], [(0.1111111111111111, 0), (0.2222222222222222, 0), (0.16666666666666666, 0), (0.3333333333333333, 0), (0.05555555555555555, 0), (0.1111111111111111, 0)], [(0.2222222222222222, 0), (0.1111111111111111, 0), (0.3333333333333333, 0), (0.16666666666666666, 0), (0.1111111111111111, 0), (0.05555555555555555, 0)], [(0.2222222222222222, 0), (0.4444444444444444, 0), (0.1111111111111111, 0), (0.6, 0), (0, 0), (0, 0)], [(0.4444444444444444, 0), (0.2222222222222222, 0), (0.2222222222222222, 0), (0.1111111111111111, 0), (0, 0), (0, 0)]])
    def test_experimentos(self):
        estado=[(4/5,0),(1/5,0),(0,0),(0,0),(0,0),(0,0)]

        matriz=[[(0,0),(0,0),(1/18,0),(1/9,0),(5/18,0),(5/9,0)],
           [(0,0),(0,0),(1/9,0),(1/18,0),(5/9,0),(5/18,0)],
           [(1/9,0),(2/9,0),(1/6,0),(1/3,0),(1/18,0),(1/9,0)],
           [(2/9,0),(1/9,0),(1/3,0),(1/6,0),(1/9,0),(1/18,0)],
           [(2/9,0),(4/9,0),(1/9,0),(2/9,0),(0,0),(0,0)],
           [(4/9,0),(2/9,0),(2/9,0),(1/9,0),(0,0),(0,0)]]
        click=1
        self.assertEqual (experimentos(matriz,estado,click) , [(0.0, 0.0), (0.0, 0.0), (0.13, 0.0), (0.2, 0.0), (0.27, 0.0), (0.4, 0.0)])

if __name__ == '__main__':
        unittest.main()
