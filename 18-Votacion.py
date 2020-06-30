print('Bienvenido al simulador de votación')

nombre = input('Por favor escribe tu nombre: ').title()

while True:
    edad = input('Por favor ingresa tu edad: ')
    try:
        edad = int(edad)
        if edad < 18:
            print('Aún no puedes votar')
            break
        else:
            break
    except:
        print('Introduce solo números enteros')

partidos = ['Morena','PAN','PRI']
partidos_min = ['MORENA','PAN','PRI']

if edad >= 18:
    print('\nGenial, puedes votar\nAquí estan los partidos políticos por los que puedes votar:\n ')
    for partido in partidos:
        print('\t- ' + partido)
    while True:
        eleccion = input('\nPor cuál partido quieres votar?: ').upper()
        if eleccion == 'MORENA':
            print('\n¡Bien hecho ' + nombre + '!, haz votado por ' + partidos[0])
            break
        elif eleccion == 'PAN':
            print('\n¡Bien hecho ' + nombre + '!, haz votado por ' + partidos[1])
            break
        elif eleccion == 'PRI':
            print('\n¡Bien hecho ' + nombre + '!, haz votado por ' + partidos[2])
            break
        else:
            print('Opción no válida')
else:
    print('Vuelve cuando seas mayor de edad')