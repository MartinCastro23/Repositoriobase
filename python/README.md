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
### Sintaxis
if (condición) operador x:
En phyton existe la funcion input() que sirve para introducir datos por el teclado. Lo que recive un imput lo transforma en datos de texto.
El ambito de una variable es la parte del programa en la que es accesible una variable.
El if puede ir acmpañado de else(y si no es verdad) que se ejecuta cuando la condicion da como resultado falso. El else siempre es compañero del if más cercano.
