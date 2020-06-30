from datetime import datetime
import random
import time


lista = ['Carne','Queso']
print('Bienvenido al Simular de Tienda')
fecha = datetime.now()
print('Fecha y hora: ' + str(fecha.month) + '/' + str(fecha.day) + '\t' + str(fecha.hour) + ':' + str(fecha.minute))
print('Actualmente tienes: ' + ', '.join(lista) + '\n')

nuevo_elemento = input('Escribe para agregar un nuevo elemento: ').title()
lista.append(nuevo_elemento)
nuevo_elemento = input('Escribe para agregar un nuevo elemento: ').title()
lista.append(nuevo_elemento)
nuevo_elemento = input('Escribe para agregar un nuevo elemento: ').title()
lista.append(nuevo_elemento)

print(f'\nAsí esta tu lista actualmente: \n {lista}')
lista.sort()
print(f'\nAsí esta tu lista organizada:\n {lista}')
#time.sleep(1.5)
print('\nSimulando compras...\n')

print('Actualmente hay en la tienda ' + str(len(lista)) + ' elementos')
print(lista)
print('Compra 3 elementos:\n')

while True:
    compra = input('¿Qué deseas comprar?: ').title()
    if compra in lista:
        print('¡Buena compra!')
        print('Quitando ' + compra + ' de la lista...')
        lista.remove(compra)
        break
    else:
        print('No tenemos eso en la tienda...intenta otra vez\n')
        continue

print('\nActualmente hay en la tienda ' + str(len(lista)) + ' elementos')
print(lista)
print('Compra 2 elementos:\n')

while True:
    compra = input('¿Qué deseas comprar?: ').title()
    if compra in lista:
        print('¡Buena compra!')
        print('Quitando ' + compra + ' de la lista...')
        lista.remove(compra)
        break
    else:
        print('No tenemos eso en la tienda...intenta otra vez\n')
        continue

print('\nActualmente hay en la tienda ' + str(len(lista)) + ' elementos')
print(lista)
print('Compra 1 elemento:\n')

while True:
    compra = input('¿Qué deseas comprar?: ').title()
    if compra in lista:
        print('¡Buena compra! ¡Hasta luego!')
        print('Quitando ' + compra + ' de la lista...')
        lista.remove(compra)
        break
    else:
        print('No tenemos eso en la tienda...intenta otra vez\n')
        continue

print('\n****VOLVIENDO AL MODO VENDEDOR****\n')

print('\nActualmente hay en la tienda ' + str(len(lista)) + ' elementos')
print(lista)

print('\nOops, parece que ya no hay ' + lista[1])
lista.pop(1)
nuevo_elemento = input('¿Qué te gustaría agregar en su lugar? ').title()
lista.insert(0,nuevo_elemento)
print('Así quedó la lista:\n' + str(lista))