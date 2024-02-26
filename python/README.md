# PYTHON
Python es un lenguaje de alto nivel, porque se parece al lenguaje humano en su sintaxis.
Un lenguaje de bajo nivel es uno con muchos números, cerca del lenguaje binario (ceros y unos). 

Tiene un tipado dinamico (la formación se hace sobre la marcha) y fuerte (diferencia claramente los tipos de variable).

Una variable puede tener números, pero no puede empezar por uno, mayúscula o serpientes.

#### Reglas de cortesia:
Empezar por minúscula/Tener serpientes

## Tipos
- tipos de texto: cadenas(str)

- tipos numericos:enteros(int), decimales(float) y complejos(complex)

- tipos de secuencia: listas(list), tuplas(tuple) y rangos(range)

- tipos de mapeado: diccionarios(dict)

- tipos boleanos: boleanos(bool)

## Operadores:
- ### Aritmeticos:
-Suma (+)  -Resta (-)  -Multiplicación (*)  -División (/)  -Módulo (%)  -Exponente (**)  -División entera (//)
- ### Comparación:
-Igual que (==)  -Diferente que (!=)  -Mayor que (>)  -Menor que (<)  -Mayor o igual que (>=)  -Menor o igual que (<=)
- ### Lógicos:
-AND  -OR  -NOT
- ### Asignación:
-Igual (=)  -Incremento (+=)  -Decremento (-=)  -Producto (*=)  -División (/=)  -Resto (%=)  -Exponente (**=)  -Cociente (//=)
- ### Especiales:
-IS  -IS NOT  -IN  -NOT IN 

## Identación: 
 Las líneas identadas forman bloque con la anterior sin identar, para esto se usa la tabulación o cuatro espacios.

## Variable: 
 Espacio en la memoria del ordenador donde se almacenará un valor que podra cambiar durante la ejecución del programa.A la variable se les asigna un nombre para poder referirnos a ellas.

## Listas
- ### ¿Qué son las listas?
Estructura de datos que nos permite almacenar gran cantidd de valores. En phyton las listas pueden guardar diferentes tipos de valores. Se pueden expndir dinámicamente añadiendo nuevos elementos.
- ### Sintaxis de las listas
Las listas tienen índice(elem1: índice 0, elem2: índice 2 ...)

nombreLista=[elem1, elem2, elem3]      
print (nombreLista)  (imprime todos los elem)
print (nombreLista(1))  (imprime el de índice 1, elem2)
print (nombreLista(-1))  (imprime el 1º por el final, elem3)

## Estructuras de control de flujo
### Flujo de ejecución de un programa
- Programa: orden con el que se ejecucion tus instrucciones
En phyton el orden normal es de arriba a abajo.
Las estructuras condicionales pueden romper el flujo. Las condiciones a avaliar dan como resultado verdadero o falso. Si da verdadero se ejecuta el bloque, y si da falso no se ejecuta nada, rompe el flujo normal.
### Sintaxis (examen)
if (condición) operador x:
En phyton existe la funcion input() que sirve para introducir datos por el teclado. Lo que recive un imput lo transforma en datos de texto.
El ambito de una variable es la parte del programa en la que es accesible una variable.
El if puede ir acmpañado de else(y si no es verdad) que se ejecuta cuando la condicion da como resultado falso. El else siempre es compañero del if más cercano.

## Elif 
Se usa cuando tenemos que asignar muchas condiciones y todas estan integradas. Es una combinación entre if y else.

## Condicionales
Con catenación de operadores de comparación, el resultado es verdadero si todo es verdadero. if 0<edad>100
Solo se puede hacer si son de la misma medida.

##boleanos
and, or y not son operadores boleanos.
- And: para que salga la condición verdadera tiene que salir las dos verdaderas.
- Or: sale verdadero si uno es verdadero
- Not: si es falso es verdadero
En los condicionales podemos usar también el comando in. Este sirve para comprobar si una palabra esta dentro de una secuencia.

##Bucles
Los bulces pueden ser determinados cuando sabemos cuantas veces se va a repetir, y los indeterminados son cuando se repiten una cantidad indeterminada de veces(dependen de una condicion).
Se forma por la declaracion y cuerpo del bucle. Cuando se entra en un bucle el programa no avanza hasta que se salga de el.
Cuando el elemento es una lista la variable vale los elementos de la lista por orden, y si es una cadena de texto valen sus caracteres. 
La función range develve una lista de números enteros empezando por el 0, y de tantos elementos como se le paso por el parámetro, 
o si se meten dos parámetros(el de la iqzierda tiene que ser menor), me va a devolver una cantidad de números enteros que es la resta empezando por el menor.
La función "print" es formateable, para eso lo primero dentro del paréntesis es la letra f. 
Primero empezamos con la letra f y luego podem usar varibles con substitución poniendo la variable entre paréntesis.
ej:
i =perico
print(f"buenos dias {i}")
resultadp:  benos dias perico

###Sintaxis bucles (examen)  
for variable a recorrer in elemento a recorrer(lista, tupla, cadena de texto y rango):

###Práctca de bucle for
Introducimos una frase por texto, y creamos una funcion que me cuente cuántas vocales hay  en ese texto.

###While sintaxis (examen)
while condición:
