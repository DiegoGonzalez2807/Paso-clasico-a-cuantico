import libreria1
def probabilidad(vector,i):
    a = libreria1.modulos(vector[i])
    a = a**2
    b = libreria1.norma(vector)
    b = b**2
    respuesta = a/b
    return respuesta
def main():
    i = 2
    vector = [(-3,-1),(0,-2),(0,1),(2,0)]
    respuesta = probabilidad(vector,i)
    print(respuesta)
main()
