import math
def suma(c,d):
    sum1  = c[0] + d[0]
    sum1 = round(sum1, 2)
    sum2 =  c[1] + d[1]
    sum2 = round(sum2, 2)
    return(sum1,sum2)
def resta(c,d):
    rest1 =  c[0] - d[0]
    rest1 = round(rest1, 2)
    rest2 = c[1] - d[1]
    rest2 = round(rest2, 2)
    return (rest1,rest2) 
def multi(c,d):
    multi1 =  (c[0] * d[0] )- (c[1] * d[1])
    multi1 = round(multi1, 2)
    multi2 = (c[0] * d[1]) + (c[1] * d[0])
    multi2 = round(multi2, 2)
    return (multi1,multi2)
def division(c,d):
    numerador1 = c[0] * c[1] + d[0] * d[1]
    denominador1 = c[1]**2 + d[1]**2
    numerador2 = c[1] * d[0] - c[0] * d[1]
    denominador2 = c[1]**2 + d[1]**2
    divisor1 = numerador1 / denominador1
    divisor1 = round(divisor1, 2)
    divisor2 = numerador2 / denominador2
    divisor2 = round(divisor2, 2)
    return(divisor1,divisor2)
def conjugado(c):
    return c[0] , c[1]*-1
def modulos(c):
    raiz = math.sqrt(c[0]**2 + c[1]**2)
    raiz = round(raiz, 2)
    return (raiz,0)
def cartesiapolar(c):
    p = math.sqrt(c[0]**2 + c[1]**2)
    p = round(p, 2)
    tetha = math.atan2(c[0],c[1])
    tetha = round(tetha, 2)
    return (p,tetha)
def retorno(c):
    tetha = math.atan2(c[1],c[0])
    tetha = round(tetha, 2)
    return (tetha,0)
def sumavector(a,b):
    matriz =[]
    m = len(a)
    for i in range (m):
        sum1 = suma(a[i],b[i])
        matriz = matriz + [sum1]
    return matriz
def inversa(c):
    matriz = []
    a = (-1,0)
    for i in range(len(c)):
        mult1 = multi(c[i],a)
    matriz = matriz + [mult1]
    return matriz
def multiescalar(a,d):
    matriz = []
    i = 0
    for i in range(len(a)):
        matriz = matriz + [multi(a[i],d)]
    print(matriz)
    return matriz
def sumaMatriz(a,b):
    n,m = len(a),len(b)
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = suma(a[i][j],b[i][j])
    print(c)
    return c
def inversaMatriz(g):
    n,m = len(g),len(g[0])
    i = 0
    j = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = multi(g[i][j],(-1,0))
    print(c)
    return c
def escalarmatrices(h,l):
    n,m = len(h), len(h[0])
    i = 0
    j = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = multi(h[i][j], l)
    print(c)
    return c
def transpuesta(y):
    n,m = len(y),len(y[0])
    i = 0
    j = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = y[j][i]
    return c
def conjumatrices(z):
    n,m = len(z),len(z[0])
    i = 0
    j = 0
    c = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = conjugado(z[i][j])
    return c
def adjunmatrices(a):
    c = transpuesta(conjumatrices(a))
    return c
def accionmatvector(a,b):
    n,m = len(a), len(a[0])
    prob1 = len(b)
    arreglo = []
    if prob1 == m:
        matinicial = (0,0)
        for i in range(n):
            for j in range(m):
                resultado = multi(a[i][j],b[j])
                Sum1 = suma(matinicial,resultado)
            arreglo = arreglo + [Sum1]
            Sum1 = (0,0)
    return arreglo

def multimatriz(a,b):
    n,m = len(a),len(a[0])
    d,f = len(b),len(b[0])
    c = transpuesta(b)
    matriz = []
    acumulador = []
    cont = 0
    c = [[(0,0) for j in range(m)]for i in range(n)]
    if m == d:
        for k in range(f):
            for i in range(n):
                for j in range(m):
                    p = multi(a[k][j], b[i][j])
                    matriz = matriz + [p]
            for i in range(n):
                for j in range(m):
                    while cont <= len(matriz)-1:
                        acumulador = acumulador + [suma(matriz[cont],matriz[cont+1])]
                        cont = cont + 2
    return matriz
def interno(a,b):
    vector = (0,0)
    m,n = len(a),len(b)
    for i in range(m):
        resp1 = conjugado(a[i])
        respuesta2 = multi(resp1,b[i])
        respuesta = suma(vector,respuesta2)
    return respuesta
def potencia(a):
    for i in range(len(a)):
        c = multi(a,a)
    return c
def norma(a):
    e = interno(a,a)
    c = (e[0]) ** (1/2)
    c = round(c,2)
    return c
def distancia(d,e):
    b = inversa(e)
    c = sumavector(d,e)
    h = interno(c,c)
    respuesta = (h[0] ** (1/2))
    respuesta = round(respuesta,2)
    return respuesta
def revisionunitaria(a):
    respuesta = False
    b = adjunmatrices(a)
    c = multimatriz(a,b)
    if a == c:
        respuesta = True
        print(respuesta)
        return respuesta
    else:
        respuesta = False
        print(respuesta)
        return respuesta
def revisionhermitiana(a):
    respuesta = False
    b = adjunmatrices(a)
    if b == a:
        respuesta = True
        print(respuesta)
        return respuesta
    else:
        respuesta = False
        print(respuesta)
        return respuesta
def tensor(a,b):
    arreglo = []
    posi = 0
    posj = 0
    while posi < (len(a)-1)*2:
        fila1 = a[posi]
        fila2 = b[posj]
        fila3 = []
        for i in fila1:
            for j in fila2:
                fila3 = fila3 + [multi(i,j)]
        posj = posj + 1
        fila2 = b[posj]
        arreglo.append(fila3)
        fila = []
        for i in fila1:
            for j in fila2:
                fila.append(multi(i,j))
        posi = posi + 1
        posj = posj - 1
        arreglo.append(fila)
    return arreglo
def prettyprinting(a):
    print(a[0], "+", a[1], "i")
def main():
    vector1 = [(1,0),(2,3)]
    vector2 = [(3,4),(4,6)]
    matriz1 =  [(1,0),(2,3)], [(3,4),(4,6)],
    matriz2 = [(2,1),(3,5)], [(3,7),(4,8)],
    num1 = (3,0)
    num2 = (3.7,8.5)
    num3 = (2,0)
    sumar = suma(num2,num1)
    restar = resta(num2,num1)
    multiplicacion = multi(num2,num1)
    dividir = division(num2,num1)
    conjugar = conjugado(num2)
    modulo = modulos(num2)
    cambiocoordenadas = cartesiapolar(num2)
    retornar = retorno(num2)
    prettyprinting(sumar)
    prettyprinting(restar )
    prettyprinting(multiplicacion)
    prettyprinting(dividir)
    prettyprinting(conjugar)
    prettyprinting(modulo)
    prettyprinting(cambiocoordenadas)
    prettyprinting(retornar)
    sumar1 = sumavector(vector2,vector1)
    print(sumar1)
    multi2 = multiescalar(vector1,num3)
    sumar2 = sumaMatriz(matriz1,matriz2)
    invertir1 = inversaMatriz(matriz1)
    escalar1 = escalarmatrices(matriz1,num3)
    transponer1 = transpuesta(matriz1)
    print(transponer1)
    conjugar1 = conjumatrices(matriz1)
    print(conjugar1)
    adjuntar1 = adjunmatrices(matriz1)
    print(adjuntar1)
    multiplicar1 = multimatriz(matriz1,matriz2)
    print(multiplicar1)
    accion1 = accionmatvector(matriz1, vector1)
    print(accion1)
    prodpunto1 = interno(vector1, vector2)
    print(prodpunto1)
    norma1 = norma(vector1)
    print(norma1)
    distancia1 = distancia(vector1,vector2)
    print(distancia1)
    unitaria1= revisionunitaria(matriz1)
    hermitiana1 = revisionhermitiana(matriz1)
    productotensor1 = tensor(matriz1,matriz2)
    print(productotensor1)
main()
