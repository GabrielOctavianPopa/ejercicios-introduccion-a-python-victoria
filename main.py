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
#
# # 1.El mayor número de la lista
# print('El mayor número de la lista: ', max(x))
#
# # 2.El menor número de la lista
# print('El menor número de la lista: ', min(x))
#
# # 3.Los tres mayores números de la lista
# print('Los tres mayores números de la lista: ', end='')
# x.sort()
# for i in range(3):
#     print(x[len(x) - 1 - i], end=' ')
#
# # 4.El mayor de los 3 primeros números de la lista
# print('')
# print('El mayor de los 3 primeros números de la lista: ', end='')
# x.sort()
# print(x[2])
#
# # 5.El menor de los 4 últimos números de la lista
# print('El menor de los 4 últimos números de la lista: ', end='')
# x.sort()
# print(x[4])
#
# # 6.La suma de los 5 mayores números de la lista
# print('La suma de los 5 mayores números de la lista: ', end='')
#
# # 7.La suma de los 3 menores números de la lista
# print('La suma de los 3 menores números de la lista: ', end='')
# x.sort()
# print(x[0] + x[1] + x[2])

