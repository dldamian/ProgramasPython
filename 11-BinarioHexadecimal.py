import time

print('Bienvenido al convertidor de Decimales a Binarios y Hexadecimales\n')

while True:
    decimal = input('Generaremos una lista de decimales, binarios y hexadecimaneles.\n ¿Hasta que número quieres generar la lista?: ')
    try:
        decimal = int(decimal)
        if decimal <= 0 or decimal == 1:
            print('Error. Escribe al menos 2 o más')
        else:
            break
    except:
        print('Solo números enteros')

print('\nGenerando listas...')
lista_decimales = list(range(1,decimal+1))
binarios = [bin(binario) for binario in range(1,decimal+1)]
hexadecimales = [hex(hexa) for hexa in range(1,decimal+1)]

time.sleep(1)

print('Listo\n')
print('Usando "slices", vamos a mostrar solo una porción de la lista.')

while True:
    empieza = input('¿Con qué decimal te gustaría empezar?: ')
    try:
        empieza = int(empieza)
        if empieza <= 0 or empieza >= decimal:
            print('Error. No podríamos mostrar datos a partir del valor que elegiste')
        else:
            break
    except:
        print('Solo números enteros')

while True:
    termina = input('¿Con qué decimal te gustaría terminar?: ')
    try:
        termina = int(termina)
        if termina <= empieza or termina > decimal:
            print('Error. No podríamos mostrar datos a partir del valor que elegiste')
        else:
            break
    except:
        print('Solo números enteros')

print('\nValores decimales del ' + str(empieza) + ' al ' + str(termina))
for i in lista_decimales[empieza-1:termina]:
    print(i)

print('\nValores binarios del ' + str(empieza) + ' al ' + str(termina))
for i in binarios[empieza-1:termina]:
    print(i)

print('\nValores hexadecimales del ' + str(empieza) + ' al ' + str(termina))
for i in hexadecimales[empieza-1:termina]:
    print(i)

input('\nPresiona ENTER para ver toda la tabla: ')
print('Decimal ----- Binario ----- Hexadecimal')
print('-'*50)
for d,b,h in zip(lista_decimales,binarios,hexadecimales):
    print(str(d) + ' ----- ' + str(b) + ' ----- ' + str(h))