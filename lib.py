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
    
def prettyprinting(a):
    print(a[0], "+", a[1], "i")
def main():
    b = (3,0)
    a = (3.7,8.5)
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
   
main()
    
