#coding=utf-8
#esta linea imprime hola mundo
print('hola mundo')
print('\'Hola\' todos')
print(3.141592)
print('Parte izq  ' + 'Parte drch')
print('el numero Pi es  ' + str(3.141592))

print('3' + '5')
print(3 + 5)
print('3+5')
#declaracion de varibles: darles un nombre y un valor
frase = 'Hola itagui  '
otra_frase = 'me gusta vivir aca'
print(frase + otra_frase)
print(frase + '\n' + otra_frase)
Frase = 12.31
print(type(otra_frase))
print(type(Frase))
print(type(str(Frase)))

#Operaciones aritmeticas
# + - Suma y resta
# * - Multiplicacion
# / - Division
# ** - Potencia
# // - Division entera

print(4 + 21)
print(6 - 2)
print(4 * 2)
print(2**4)
print(14 / 3)
print(14 // 3)
print(125**(1 / 3))
print(25**(1 / 2))
print(3 + 12 * 5 + 27 / 3)

print(3 + 12 * (5 + 27) / 3)

nombre = input('cual es tu nombre?')
print('hola ' + nombre)

#Programa que prefunte una hora y diga cuantos minutos son
horas = input('cuantas horas?')
minutos = 60 * float(horas)
print('la cantidad de minutos es ', minutos)
