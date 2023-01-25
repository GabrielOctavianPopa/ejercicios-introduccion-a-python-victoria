#Gabriel Octavian Popa

'''
1. EJERCICIOS CONDICIONALES
'''

# # 1. Escribe un programa que pida al usuario un número del 1 al 7 e imprima el día de la semana correspondiente.
# numeroEj1 = int(input("Introduce un número del 1 al 7: "))
# while(numeroEj1 < 1 or numeroEj1 > 7):
#     numeroEj1 = int(input("Introduce un número del 1 al 7: "))
# if(numeroEj1 == 1):
#     print("Lunes")
# elif(numeroEj1 == 2):
#     print("Martes")
# elif(numeroEj1 == 3):
#     print("Miércoles")
# elif(numeroEj1 == 4):
#     print("Jueves")
# elif(numeroEj1 == 5):
#     print("Viernes")
# elif(numeroEj1 == 6):
#     print("Sábado")
# elif(numeroEj1 == 7):
#     print("Domingo")
#
# # 2. Escribe un programa que pida al usuario tres números y muestre el mayor de ellos.
# numero1Ej2 = int(input("Introduce el primer número: "))
# numero2Ej2 = int(input("Introduce el segundo número: "))
# numero3Ej3 = int(input("Introduce el tercer número: "))
# if(numero1Ej2 > numero2Ej2 and numero1Ej2 > numero3Ej3):
#     print("El mayor es el primero")
# elif(numero2Ej2 > numero1Ej2 and numero2Ej2 > numero3Ej3):
#     print("El mayor es el segundo")
# elif(numero3Ej3 > numero1Ej2 and numero3Ej3 > numero2Ej2):
#     print("El mayor es el tercero")
#
# # 3. Escribe un programa que pida al usuario dos números y muestre el resultado de la división del primer número por el
# # segundo, siempre y cuando el segundo número sea distinto de 0. Si el segundo número es 0, el programa debe mostrar un mensaje de error.
# numero1Ej3 = int(input("Introduce el primer número: "))
# numero2Ej3 = int(input("Introduce el segundo número: "))
# while(numero2Ej3 == 0):
#     numero2Ej3 = int(input("El segundo numero no puede ser 0, introduce el segundo número: "))
# print(numero1Ej3/numero2Ej3)

# # 4. Escribe un programa que pida al usuario un número y muestre si es primo
# numeroEj4 = int(input("Introduce un número: "))
# if(numeroEj4 == 1):
#     print("El número es primo")
# else:
#     for i in range(2, numeroEj4):
#         if(numeroEj4 % i == 0):
#             print("El número no es primo")
#             break
#     else:
#         print("El número es primo")

'''
2. EJERCICIOS BUCLES
'''

# # 1.Imprime por pantalla todas las potencias de 3 menores o iguales que 2048, utilizando un bucle while.
# numeroEj1 = 3
# while(numeroEj1 <= 2048):
#     print(numeroEj1)
#     numeroEj1 = numeroEj1 * 3

# # 2.Lee valores del usuario hasta que teclee un número par, utilizando un bucle while.
# numeroEj2 = int(input("Introduce un número: "))
# while(numeroEj2 % 2 != 0):
#     numeroEj2 = int(input("Introduce un número par: "))
# print("El número es par")

# # 3.Imprime por pantalla todas las posiciones de la letra ‘s’ en la cadena: “Sistemas de gestión empresarial”
# cadenaEj3 = "Sistemas de gestión empresarial"
# for i in range(len(cadenaEj3)):
#     if(cadenaEj3.lower()[i] == "s"):
#         print(i)

# # 4. Escribe un programa que calcule el factorial de un número utilizando un for.
# numeroEj4 = int(input('Introduce un numero: '))
# factorial = 1
# for i in range(1, numeroEj4 + 1):
#     factorial = factorial * i
# print(factorial)

'''
3. EJERCICIOS CADENAS
'''

# cadena = 'Mi nombre completo es Gabriel Octavian Popa'
# # 1.¿El tamaño de la cadena?
# print('Tamaño de la cadena: ', len(cadena))
#
# # 2.Los primeros tres caracteres de la cadena.
# iterador = 0
# print('Los tres primeros caracteres de la cadena son: ', end='') # end='' para que no salte de linea
# while(iterador < 3):
#     print(cadena[iterador], end='')
#     iterador = iterador + 1
#
# # 5.Los últimos diez caracteres, de tres en tres.
# iterador = len(cadena) - 10
# print('')
# print('Los últimos diez caracteres de la cadena son: ', end='')
# while(iterador < len(cadena)):
#     print(cadena[iterador], end='')
#     iterador = iterador + 3
#
# # 6.En mayúscula, los caracteres en posiciones múltiplo de tres.
# iterador = 0
# print('')
# print('Los caracteres en posiciones múltiplo de tres en mayúscula son: ', end='')
# while(iterador < len(cadena)):
#     if(iterador % 3 == 0):
#         print(cadena[iterador].upper(), end='')
#     else:
#         print(cadena[iterador], end='')
#     iterador = iterador + 1
#
# # 7.De dos en dos, del carácter en la posición 3 al de la 20.
# iterador = 3
# print('')
# print('Los caracteres de dos en dos, del carácter en la posición 3 al de la 20 son: ', end='')
# while(iterador < 20):
#     print(cadena[iterador], end='')
#     iterador = iterador + 2
#
# # 8.¿Está el carácter “d" en la cadena?
# print('')
# print('¿Está el carácter “d" en la cadena?: ', end='')
# if('d' in cadena):
#     print('Si')
# else:
#     print('No')
#
# # 9.¿Y “a", en mayúscula o minúscula?
# print('¿Está el carácter “a" en la cadena?: ', end='')
# if(cadena.lower().find('a') != -1):
#     print('Si')
# else:
#     print('No')
#
# # 10.Divide la cadena en palabras y une las palabras con guiones.
# print('Divide la cadena en palabras y une las palabras con guiones: ', end='')
# print(cadena.replace(' ', '-'))
#
# # 11.Cuenta las vocales que tiene
# vocales = ['a', 'e', 'i', 'o', 'u']
# contadorVocales = 0
# for i in range(len(cadena)):
#     if(cadena.lower()[i] in vocales):
#         contadorVocales = contadorVocales + 1
# print('La cadena tiene ', contadorVocales, ' vocales')
#
# # 12.Remplaza las o por 0.
# print('Remplaza las o por 0: ', end='')
# print(cadena.replace('o', '0').replace('O', '0'))

'''
4. EJERCICIOS LISTAS
'''
# Manipulación de listas

# lista = ["nombre", 3, "4.5", 7.0, "apellidos"]
#
# # 1.¿El tamaño de la lista?
# print('Tamaño de la lista: ', len(lista))
#
# # 2.Recorre la lista.
# print('Recorre la lista: ', end='')
# for i in range(len(lista)):
#     print(lista[i], end=' ')
#
# # 3.El tamaño de la lista multiplicado por su segundo elemento
# print('')
# print('El tamaño de la lista multiplicado por su segundo elemento: ', len(lista) * lista[1])
#
# # 4.¿Está 7 en la lista? ¿Y 7.0? El producto del segundo elemento de la lista por el tercero
# print('¿Está 7 en la lista?: ', end='')
# if(7 in lista):
#     print('Si')
# else:
#     print('No')
#
# print('El producto del segundo elemento de la lista por el tercero: ', lista[1] * float(lista[2]))
#
# # 5.Eliminar el primer elemento de la lista
# print('Elimina el primer elemento de la lista: ', end='')
# lista.pop(0)
# for i in range(len(lista)):
#     print(lista[i], end=' ')
#
# # 6.Eliminar ahora los dos últimos elementos simultáneamente
# print('')
# print('Elimina los dos últimos elementos simultáneamente: ', end='')
# lista.pop()
# lista.pop()
# for i in range(len(lista)):
#     print(lista[i], end=' ') # despues del pop del ejercicio 5 la lista tiene un elemento menos
#
#
# # 7.¿Está la lista vacía?
# print('')
# print('¿Está la lista vacía?: ', end='')
# if(len(lista) == 0):
#     print('Si')
# else:
#     print('No')

# ordenacion de listas

# x = [9, 2, 3, 10, 7, 3, 10, 3, 9]
# # numero maximo
# print(max(x))
# # numero minimo
# print(min(x))
# # los tres mas grandes
# print(sorted(x)[-3:])
# # los tres mas pequeños
# print(sorted(x)[:3])
# # el mayor de los tres primeros
# print(max(x[:3]))
# # el menor de los cuatro ultimos
# print(min(x[-4:]))
# # la suma de los 5 mayores numeros de la lista
# print(sum(sorted(x)[-5:]))
# # la suma de los 3 menores numeros de la lista
# print(sum(sorted(x)[:3]))

# listas finales

# # 1 Realiza un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10.)
# # a continuacion debe mostrar todas las notas, la nota media, la nota mas alta que ha sacado y la menor
#
# print("Introduce las 5 notas: ")
# notas = []
# contadorAux = 0;
# while (contadorAux < 5):
#     nota = float(input())
#     if (nota >= 0 and nota <= 10):
#         notas.append(nota)
#         contadorAux += 1
#     else:
#         print("Nota no valida")
#
# print("Notas: ", notas)
#
# print("Nota media: ", sum(notas) / len(notas))
#
# print("Nota mas alta: ", max(notas))
# print("Nota mas baja: ", min(notas))

# # 2 Lee una cadena de texto del usuario y para cada letra indica si es una vocal o una consonante.
#
# cadena = input()
#
# for i in cadena:
#     match i.lower():
#         case 'a' | 'e' | 'i' | 'o' | 'u' | 'á' | 'é' | 'í' | 'ó' | 'ú':
#             print("Vocal")
#         case _:
#             print("Consonante")

# cadena = input()
# if cadena.isalpha():
#     for letra in cadena:
#         if letra.lower() in 'aeiouáéíóú':
#             print(letra, "vocal")
#         else:
#             print(letra, "consonante")

# # 3 A partir de 2 listas de enteros, 'numeros1' y 'numeros2', crea una lista que contiene aquellos valores
# # intersección de ambas listas.
# # de la primera que también están en la segunda e imprímela por pantalla. Es decir, calcula la
#
# numer01 = [1, 5, 6, 3, 12, 8, 9, 10, 11, 15, 26, 15, 34, 9, 20]
# numer02 = [1, 2, 3, 10, 11, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
#
# print(list(set(numer01) & set(numer02)))

# # 4 A partir de 2 listas de enteros, 'numeros1' y 'numeros2‘ de igual tamaño, generar otra cuyo primer
# # elemento es el producto del primer elemento de las listas 'numeros1' y 'numeros2', y así
# # sucesivamente.
#
# numer01 = [1, 5, 6, 3, 12, 8, 9, 10, 11, 15, 26, 15, 34, 9, 20]
# numer02 = [1, 2, 3, 10, 11, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# numer03 = []
#
# # multiplicar los elementos de las listas entre ellos y añadirlos a la lista numer03
# for i in range(len(numer01)):
#     numer03.append(numer01[i] * numer02[i])
# print(numer03)

# # 5 A partir de 2 listas de enteros, 'numeros1' y 'numeros2', almacenar en una lista el resultado de
# # multiplicar cada uno de los elementos de 'numeros1' por, a su vez, cada uno de los elementos de
# # 'numeros2'. Es decir, la lista resultante tendrá len(numeros1) * len(numeros2) elementos.
#
# numer01 = [1, 5, 6, 3, 12, 8, 9, 10, 11, 15, 26, 15, 34, 9, 20]
# numer02 = [1, 2, 3, 10, 11, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# numer03 = []
#
# # multiplicar los elementos de las listas entre ellos y añadirlos a la lista numer03
# for i in numer01:
#     for j in numer02:
#         numer03.append(i * j)
# print(numer03)

# # 6 Lee una cadena de texto del usuario e imprime por pantalla un mensaje si y solo si la cadena es un
# # palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). Ejemplo: Yo dono rosas,
# # oro no doy.
#
# cadena = input()
# cadena = cadena.replace(" ", "").lower().strip()
#
# if cadena == cadena[::-1]:
#     print("Es palindromo")
# else:
#     print("No es palindromo")

'''
6. EJERCICIOS DICCIONARIOS
'''

#  Escribir un programa que implemente un directorio. En el directorio se podrán guardar para cada dni información relativa a la persona como nombre, dirección y teléfono. El programa nos dará el siguiente menú:
# ·Añadir/modificar: Nos pide un dni. Si el dni se encuentra en el directorio, debe mostrar los datos y, opcionalmente, permitir modificarlos si no es correcto. Si el dni no se encuentra, debe permitir ingresar los datos correspondientes.
# ·Buscar: Nos pide un dni, y nos muestras el contacto. Opcionalmente podemos implementar la búsqueda por nombre.
# ·Borrar: Nos pide un dni y si existe nos preguntará si queremos borrarlo del directorio.
# ·Listar: Nos muestra todos los contactos del directorio.
#  Implementar el programa con un diccionario.

'''
 7. EJERCICIOS FUNCIONES
'''

# 1.Función que recibe una lista de enteros y devuelve la suma de todos sus elementos. Sin utilizar sum().
# 2.Función que recibe una lista de enteros y devuelve otra lista con aquellos que son pares y ≥ 113.
# 3.Función que recibe una lista de enteros y calcula su media aritmética sin utilizar el módulo maths.
# 4.Función que calcula el factorial de un número. Versión recursiva.
# 5.Función que recibe un número y devuelve una lista con todos sus divisores.
# 6. Crear una función que calcule el MCD de dos números por el método de Euclides. El método de Euclides es el siguiente:
#
# ·Se divide el número mayor entre el menor. ·Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# Crea un programa principal que lea dos números enteros y muestre el MCD.

# EJERCICIOS LISTAS POR COMPRESIÓN

x = [7, 3, 5, -6, 4, -2, 9]
#  personas = [“Carlota", “Enrique", “Ana"]
# 1.El cubo de cada elemento de la lista x.
# 2.El cuadrado de los elementos impares de x.
# 3.El cuadrado de los elementos pares y positivos de x.
# 4.Los elementos de personas con más de 5 caracteres.
# 5.Los elementos de personas que contienen la vocal “o”.
# 6.Los elementos de personas que contienen la vocal “e” y además tienen una longitud de al menos 6 caracteres.