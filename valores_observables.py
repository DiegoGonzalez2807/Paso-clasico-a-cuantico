import Particula_de_una_linea
import libreria1
def prueba_hermitiana(vector):
    prueba1 = libreria1.revisionhermitiana(vector)
def valores(matriz,estado):
    valor1 = libreria1.accionmatvector(matriz,estado)
    valor2 = Particula_de_una_linea.transito(valor1,estado)
    return valor2
def varianza(matriz2,ket):
    valor1 = valores(matriz2,ket)
    m = len(matriz2)
    n = len(matriz2[0])
    valor2 = libreria1.regla(m,n)
    valor3 = libreria1.multimatriz(valor2,libreria1.multi(valor1,(-1,0)))
    suma = libreria1.sumaMatriz(matriz2,valor3)
    respuesta = valores(libreria1.multimatriz(suma,suma),ket)
    return respuesta
