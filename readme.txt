# Calculadora de numeros imaginarios

Este proyecto es una libreria capaz de hacer operaciones básicas con tuplas de números dadas por el programa, sus operaciones son: suma,resta,multiplicacion,division,modulo,conjugado 
de numeros complejos, paso de coordenadas cartesianas a polares y el

## Comenzando 

Se empieza con la idea de que las operaciones tales como la suma y la resta de los numeros complejos es la misma que una suma de vectores, pero al llegar a la multiplicacion y division de numeros complejos se tiene que tener en cuenta la respectiva formula para que nos de el resultado correspondiente.

Para hacer la funcion conjugado, se tiene que saber que esta operacion significa dejar el numero imaginario como negativo.

Para las siguientes funciones se tiene primero que importar la biblioteca math, la cual nos ayuda con las funciones tales como la funcion seno, coseno, raiz entre otras mas.

Para la funcion modulo se necesita de la funcion raiz para poder hallar el resultado correspondiente.

Para la funcion retorno de fase se necesita de la funcion tangente^-1 para poder hallar el angulo que se requiere, el cual es el resultado total.

Para la funcion pasar de coordenadas cartesianas a polares se necesita la funcion raiz, con la cual encontramos la longitud de la recta polar, asi como tambien necesitamos la funcion tangente^-1 para hallar el angulo correspondiente. Estos dos valores encontrados forman una tupla la cual concluye el paso de coordenadas.


## Ejecucion de pruebas

Para la ejecucion de las pruebas automarizadas creadas para el programa de calculadora, se hizo un programa con el nombre de testlib(1).py con su respectivo codigo para las operaciones que se requieran probar con otros numeros.

### Analisis de pruebas 

La funcionalidad que se le da a las pruebas es poder concluir que las ocho operaciones creadas en el programa expuesto funcionen con cualquier tupla de valores, sin importar si son tuplas de numeros enteros o con decimales de maximo dos cifras.

### Tipo de pruebas

testsuma = Esta prueba tiene como finalidad testear la funcion suma de la calculadora de numeros complejos

testresta = Esta prueba tiene como finalidad testear la funcion resta de la calculadora de numeros complejos

testmulti = Esta prueba tiene como finalidad testear la funcion multiplicacion de la calculadora de numeros complejos

testdivisi = Esta prueba tiene como finalidad testear la funcion division de la calculadora de numeros complejos

testconjugado = Esta prueba tiene como finalidad testear la funcion conjugado de la calculadora para una tupla de numeros complejos

testretorno = Esta prueba tiene como finalidad testear la funcion retorno en una tupla de numeros.

testmodulos = Esta prueba tiene como finalidad testear la funcion modular en una tupla de numeros

testcartesianos = Esta prueba tiene como finalidad testear la funcion que pasa de coordenadas cartesianas a polares una tupla de numeros



## Construido con :

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Python](https://www.python.org/) - Lenguaje de programacion


## Autores ✒

* **Diego Alejandro Gonzalez Gualteros - *Documentacion*



