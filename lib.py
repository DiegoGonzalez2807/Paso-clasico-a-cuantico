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
    multi1 =  c[0] * d[0] - c[1] * d[1]
    multi1 = round(multi1, 2)
    multi2 = c[0] * d[1] + c[1] * d[0]
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
    tetha = math.atan(c[1]/c[0])
    tetha = round(tetha, 2)
    return (p,tetha)
def retorno(c):
    tetha = math.atan(c[1]/c[0])
    tetha = round(tetha, 2)
    return (tetha,0)
    
def sumamatriz(a,b):
    matriz =[]
    for i in range (2):
        sum1 = suma(a[i],b[i])
        matriz = matriz + [sum1]
    print(matriz)
def inversa(c):
    matriz = []
    a = (-1,0)
    for i in range(2):
        mult1 = multi(c[i],a)
        matriz = matriz + [mult1]
    print(matriz)
def multiescalar(a,d):
    matriz = []
    i = 0
    for i in range(2):
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
    print(c)
    return c
def conjumatrices(z):
    n,m = len(z),len(z[0])
    i = 0
    j = 0
    c = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = conjugado(z[i][j])
    print(c)
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
    return c

def multimatriz(a,b):
    n,m = len(a),len(a[0])
    d,f = len(b),len(b[0])
    c = transpuesta(b)
    matriz = []
    acumulador = []
    cont = 0
    c = [[0 for j in range(m)]for i in range(n)]
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
        print(matriz)
        return acumulador
def interno(a,b):
    m,n = len(a),len(b)
    for i in range(m):
        for j in range(n):
            resp = a[0] * b[0] + a[1] * b[1]
            resp = round(resp,2)
    print(resp)
    return resp
def potencia(a):
    for i in range(len(a)):
        c = multi(a,a)
    return c
def norma(a):
    b = potencia(a)
    c = sum(a)
    d = math.sqrt(c)
    d = round(d,2)
    print(d)
    return b
def distancia(a,b):
    c = resta(a,b)
    d = interno(c,c)
    e = math.sqrt(d)
    e = round(e,2)
    print(e)
    return c
def revisionunitaria(a):
    b = adjunmatrices(a)
    c = multimatriz(a,b)
    if a == c:
        print("La matriz es unitaria")
    else:
        print("La matriz no es unitaria")
    return b
def revisionhermitiana(a):
    b = adjunmatrices(a)
    if b == a:
        print("Matriz es hermitiana")
    else:
        print("Matriz no es hermitiana")
    return b
def prettyprinting(a):
    print(a[0], "+", a[1], "i")
def main():
    m = [(1,0),(2,3)]
    n = [(3,4),(4,6)]
    bb =  [(1,0),(2,3)], [(3,4),(4,6)],
    cc = [(2,1),(3,5)], [(3,7),(4,8)],
    b = (3,0)
    a = (3.7,8.5)
    aa = (2,0)
    c = suma(a,b)
    e = resta(a,b)
    f = multi(a,b)
    g = division(a,b)
    h = conjugado(a)
    i = modulos(a)
    j = cartesiapolar(a)
    k = retorno(a)
    prettyprinting(c)
    prettyprinting(e)
    prettyprinting(f)
    prettyprinting(g)
    prettyprinting(h)
    prettyprinting(i)
    prettyprinting(j)
    prettyprinting(k)
    l = sumamatriz(n,m)
    am = inversa(m)
    gt = multiescalar(m,aa)
    hi = sumaMatriz(bb,cc)
    hj = inversaMatriz(bb)
    hk = escalarmatrices(bb,aa)
    ac = transpuesta(bb)
    ad = conjumatrices(bb)
    ah = adjunmatrices(bb)
    ai = multimatriz(bb,cc)
    aj = potencia(a)
    ak = norma(a)
    al = interno(a,b)
    am = distancia(a,b)
    an = revisionunitaria(bb)
    ao = revisionhermitiana(bb)
    ap = accionmatvector(bb,a)
main()
