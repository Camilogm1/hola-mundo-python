#coding=utf-8

#Programa que lee un dato de hora y lo convierte a minutos
#entrada: Valor de la hora
#Salida: Valor de la hora en minutos  

print('Este programa lee un dato de hora y lo convierte a minutos')
Dato_hora = input('cuantas horas?')
print('El tipo de dato de la variable horas es ', type(Dato_hora))

#Indentificamos si en la cadena hay el caracter "."
if '.' in Dato_hora:
  #si el caracter "." entonces se convierte a float
  Dato_hora = float(Dato_hora)
else:
  #si no hay el caracter "." entonces se convierte a int
  Dato_hora = int(Dato_hora)

#Se calcula el valor de la hora en minutos
minutos= Dato_hora * 60

print(f'las horas {Dato_hora}convertidas en minutos son: ', {minutos})
print  ('el tipo de dato de la variable minutos es ', type(minutos))

muchos_minutos = 120

if minutos > muchos_minutos:
  print('Los minutos mayores a 120, son muchos minutos')
elif minutos == muchos_minutos:
  print('Los minutos son iguales a 120, son apenas 120')
else:
  print('Los minutos menores a 120, son pocos minutos')

#programa pra identificar si una presona pude votar 
#dependiendo de su edad y nacionalidad


#tabla de verdad
#P  Q  P and Q  P or Q  
#V  V  V        V
#V  F  F        V
#F  V  F        V
#F  F  F        F

print('programa para identificar si una persona puede votar')
print('dependiendo de su edad y nacionalidad')

edad= int(input('cuantos años tienes?'))
nacionalidad= input('Ingrese su nacionalidad:')

if edad >= 18 and nacionalidad == 'Colombiano':
  print('Eres mayor de edad en colombia y puedes votar')
elif edad>= 21 and nacionalidad == 'extranjero':
  print('Eres mayor de edad en el extranjero y puedes votar')
else:
  print('Demalas, chupelo')
