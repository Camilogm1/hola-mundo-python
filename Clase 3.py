#coding utf-8

Ramas=1
while Ramas <= 10:
    print('*'* Ramas )
    Ramas +=1

print('\nSegundo arbolito derecha')

Ramas = 1
Total_espacios=10
while Ramas <= 10:
    print(( ' '* Total_espacios )+('*'* Ramas))
    Ramas +=1
    Total_espacios -=1

print ('\n Tercer arbolito izq descendiente')

Rama=10
while Rama >= 1:
    print (('*'* Rama ))
    Rama-=1

print('\nCuarto arbolito drch descendiente')

Ramas=10
Total_espacios=1
while Ramas >=1:
    print ((' '* Total_espacios)+('*'* Ramas))
    Ramas-=1
    Total_espacios+=1

print('\n Quinto Arbolito centrado ')

Ramas =1
Total_espacios=11
while Ramas <=20:
    print((' '* Total_espacios)+('*'* Ramas))
    Ramas+=2
    Total_espacios-=1

print ('\n Sexto arbolito Centrado descendiente')

Rama=19
Total_espacios=1
while Rama>=1:
    print((' '* Total_espacios)+('*'* Rama))
    Rama -=2
    Total_espacios+=1

print('\septimo arbolito centrado sin espacio')

Rama=2
Nrama=3
Espacio=11
Espacio_central=0
while Rama >=11:
    print((' '* Espacio)+ ('*'* Rama))
    Espacio-=1
    Espacio_central+=1
    Nrama+=1
    Rama +=1

Ramas = 1
Total_espacios = 11

while Ramas <= 20:
    if Ramas == 1:
        print(' ' * Total_espacios + '*')  # Imprime la punta del árbol
    else:
        print(' ' * Total_espacios + '*' + ' ' * (Ramas - 2) + '*')  # Imprime solo los extremos
    Ramas += 2
    Total_espacios -= 1
