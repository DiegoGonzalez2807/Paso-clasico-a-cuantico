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

testsumavector = Esta prueba tiene como finalidad testear la funcion que suma dos vectores definidos de numeros complejos

testmultiescalar = Esta prueba tiene como finalidad testear la funcion que multipica un vector definido de numeros complejos con un valor escalar cualquiera

testsumamatriz =  Esta prueba tiene como finalidad testear la funcion que suma dos matrices definidas por tuplas de numeros complejos.

testinversamatriz  =  Esta prueba tiene como finalidad testear la funcion que invierte los signos de una matriz definida por tuplas de numeros complejos.

testescalarmatriz =  Esta prueba tiene como finalidad testear la funcion que multiplica una matriz definida por tuplas de numeros complejos por un numero escalar cualquiera.

testtranspuesta = Esta prueba tiene como finalidad testear la funcion que cambia las filas de una matriz definida por tuplas de numeros complejos por columnas definidas de igual manera.

testconjugadomatriz = Esta prueba tiene como finalidad testear la funcion que invierte los signos de la parte imaginaria de la tuplas de numeros complejos que definen la matriz.

testadjuntamatriz = Esta prueba tiene como finalidad testear la funcion que conjuga la matriz (cambia los valores de la parte imaginaria de las tuplas de la matriz) y la transpone (cambiar las filas de la matriz por columnas y hacer el mismo proceso con las columnas de esta misma).

testmultimatrices = Esta prueba tiene como finalidad testear la funcion que multiplica dos matrices de igual tamaño, las cuales ambas estan definidas por tuplas de numeros imaginarios.

testaccion = Esta prueba tiene como finalidad testear la funcion que multiplica un vector cualquiera por una matriz definida, ambas definidas por tuplas de numeros imaginarios, y obligatoriamente el vector tiene que tener la misma longiutd de sus filas que de la longitud de columnas de la matriz o al contrario, de que la longitud de columnas del vector sea igual a la longitud de filas de la matriz.

testinterno = Esta prueba tiene como finalidad testear el producto interno generado por dos vectores de la misma longitud, ambos definidos por tuplas de numeros imaginarios. Tener en cuenta que al tener un producto interno de numeros complejos, el primer vector se tiene que conjugar.

testnorma = Esta prueba tiene como finalidad hallar la norma o longitud absoluta de un vector, lo cual se hace haciendo el producto interno de el mismo. Este vector esta definido por tuplas de numeros complejos.

testdistancia = Esta prueba tiene como finalidad hallar la distancia total entre dos vectores definidos por tuplas de numeros imaginarios, recordar que estos dos vectores tienen que ser de la misma longitud.

testunitaria = Esta prueba tiene como finalidad decir si una matriz definida por tuplas de numernos complejos es unitaria, eso quiere decir que si la matriz se le hace la funcion adjunta y se le multiplica por la matriz origianl, tiene que dar igual a la matriz original.

testhermitiana = Esta prueba testea si una matriz definida por tuplas de numeros complejos es hermitiana, esto se sabe si esta matriz al hacerle la funcion adjunta, va a ser igual que la matriz original.

testtensor = Esta prueba tiene la finalidad de testear la funcion que multiplica cada elemento de un vector por una matriz completa, ambas definidas por tuplas de numeros complejos.




## Construido con :



* [Python](https://www.python.org/) - Lenguaje de programacion


## Autores ✒

* **Diego Alejandro Gonzalez Gualteros - *Documentacion*



