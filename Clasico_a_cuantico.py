from matplotlib import pyplot
import math
import libreria1
def experimento_canica(matriz,vector,cantidad):
    click = 0
    if len(matriz) == len(vector):
        guardar = vector
        while click != cantidad:
            guardar = libreria1.accionmatvector(matriz,guardar)
            click = click + 1
        return guardar
    else:
        print('Longitudes inexactas para hacer la accion')
        return None
def potencia (a,b):
    matriz = a
    for i in range (1,b):
        res = libreria.multimatriz(matriz,a)
        matriz=res
    return matriz

def experimentos(matriz, vector, disparo):
    res1=potencia(matriz,disparo)
    res2=lib.accionmatvector(res1,vector)
    return(res2)
def probabilidad (vector):
    x=[]
    y=[]
    for i in range (len(vector)):
        m=vector[i]
        y=y+[lib.modulos(m[0],m[1])*100]
    for i in range (len(vector)):
        x=x+[i]
    pyplot.title("PROBABILIDAD")
    pyplot.bar(x,height=y)
    pyplot.savefig("probabilidad.png")
    pyplot.show()
