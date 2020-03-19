import libreria1 
def probabilidad(vector,i):
    a = libreria1.modulos(vector[i])
    a = a**2
    b = libreria1.norma(vector)
    b = b**2
    respuesta = a/b
    respuesta = round(respuesta,2)
    return respuesta
def transito():
    r = libreria1.interno(vector,vector1)
    return r
