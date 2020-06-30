import random

print('Bienvenido a Pidra, Papel o Tijera\n')

print('INSTRUCCIONES:')
print('*'*25)
print('1) Escribe el número de rondas que quieres jugar')
print('2) Escribe el lo que quieras tirar (piedra, papel o tijera)')
print('3) Cualquier respuesta inválida contará como punto para la Computadora')
print('*'*25)

rondas = 1
puntaje_jugador = 0
puntaje_pc = 0
opciones = ['Piedra','Papel','Tijera']

while True:
    rondas_a_jugar = input('\n¿Cuántas rondas quieres jugar?: ')
    try:
        rondas_a_jugar = int(rondas_a_jugar)
        if rondas_a_jugar >= 0:
            break
        else:
            print('Escribe números mayores a 0')
    except:
        print('Escribe solo números enteros')

while rondas <= rondas_a_jugar:
    print('\nRonda ' + str(rondas))
    eleccion_user = input('Hora de escoger...(piedra, papel o tijera): ').title()
    if eleccion_user in opciones:
        eleccion_pc = opciones[random.randint(0,2)]
        print('La Computadora escogío: ' + eleccion_pc)
        if eleccion_user == 'Piedra':
            if eleccion_user == eleccion_pc:
                print('Empate')
                rondas += 1
            elif eleccion_pc == 'Papel':
                print('Punto para PC')
                rondas += 1
                puntaje_pc += 1
            else:
                print('Ganaste el punto')
                rondas += 1
                puntaje_jugador += 1
        elif eleccion_user == 'Papel':
            if eleccion_user == eleccion_pc:
                print('Empate')
                rondas += 1
            elif eleccion_pc == 'Tijera':
                print('Punto para PC')
                rondas += 1
                puntaje_pc += 1
            else:
                print('Ganaste el punto')
                rondas += 1
                puntaje_jugador += 1
        else:
            if eleccion_user == eleccion_pc:
                print('Empate')
                rondas += 1
            elif eleccion_pc == 'Piedra':
                print('Punto para PC')
                rondas += 1
                puntaje_pc += 1
            else:
                print('Ganaste el punto')
                rondas += 1
                puntaje_jugador += 1
    else:
        print('Respuesta inválida...el punto va para la Computadora')
        puntaje_pc += 1
        rondas += 1
        
print('\nResultados')
print('\tRondas jugadas: ' + str(rondas-1))
print('\tJuegos ganados por Usuario: ' + str(puntaje_jugador))
print('\tJuegos ganados por Computadora: ' + str(puntaje_pc))

if puntaje_jugador > puntaje_pc:
    print('\tGanador: Usuario')
elif puntaje_jugador < puntaje_pc:
    print('\tGanador: Computadora')
else:
    print('\tGanador: Empate')