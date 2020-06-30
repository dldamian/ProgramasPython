import random

print('Escoge tu alineación para un partido 5 vs 5\n')

jugadores = []

nuevo_jugador = input('¿Quién será tu portero?: ').title()
jugadores.append(nuevo_jugador)
nuevo_jugador = input('¿Quién será tu defensa (1/2)?: ').title()
jugadores.append(nuevo_jugador)
nuevo_jugador = input('¿Quién será tu defensa (2/2)?: ').title()
jugadores.append(nuevo_jugador)
nuevo_jugador = input('¿Quién será tu medio?: ').title()
jugadores.append(nuevo_jugador)
nuevo_jugador = input('¿Quién será tu delantero?: ').title()
jugadores.append(nuevo_jugador)

print('\n\tTu alineación para enfrentar el partido luce así:')
print('\t\tPortero: \t\t' + jugadores[0])
print('\t\tDefensa (1/2): \t\t' + jugadores[1])
print('\t\tDefensa (2/2): \t\t' + jugadores[2])
print('\t\tMedio: \t\t\t' + jugadores[3])
print('\t\tDelantero: \t\t' + jugadores[4])

azar = random.randint(0,len(jugadores)-1)
jugador_lesionado = jugadores[azar]

print('\n¡Oh no! Parece que ' + jugador_lesionado + ' está lesionado.')
jugadores.pop(azar)
print('Tu alineación solo tiene ' + str(len(jugadores)) + ' jugadores')
nuevo_jugador = input('¿Quién reemplazará a ' + jugador_lesionado + '? ').title()
jugadores.insert(azar,nuevo_jugador)

print('\n\tTu alineación para enfrentar el partido luce así:')
print('\t\tPortero: \t\t' + jugadores[0])
print('\t\tDefensa (1/2): \t\t' + jugadores[1])
print('\t\tDefensa (2/2): \t\t' + jugadores[2])
print('\t\tMedio: \t\t\t' + jugadores[3])
print('\t\tDelantero: \t\t' + jugadores[4])

print('\n¡Buena suerte!')
print('Tu alineación  tiene ' + str(len(jugadores)) + ' jugadores')
