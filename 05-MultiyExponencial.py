import math

print('Tablas/Exponenciales App')

nombre = input('Escribe tu nombre: ').strip()
mensaje = ' las Matemáticas son geniales!'
iniciador = True

while iniciador:
    num = input('¿Qué número te gustaría que trabajemos? ')
    try:
        num = float(num)
        print(f'\nTabla de Multiplicar de {num}')
        for n in range(1,11):
            print('\t' + str(n) + ' x ' + str(num) + ' = ' + str(round(n*num,4)))
        print(f'\nTabla de Exponenciales de {num}')
        for n in range(1,11):
            print('\t' + str(num) + ' ^ ' + str(n) + ' = ' + str(round(num**n,4)))
        iniciador = False
    except:
        print('Ingresa solo números')

print('\n')
print('¡' + nombre.title() + mensaje)
print('\t¡' + nombre.lower() + mensaje.lower())
print('\t\t¡' + nombre.title() + mensaje.title())
print('\t\t\t¡' + nombre.upper() + mensaje.upper())