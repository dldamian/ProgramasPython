print('Juego Gato')

nums_juego = [1,2,3,4,5,6,7,8,9]
c_vacios = ['_']*9
jugador_1 = 'X'
jugador_2 = 'O'

def tablero(lista):
    print('\n\t    Tablero')
    print('\t--------------')
    print('\t | ' + str(lista[0]) + ' | ' + str(lista[1]) + ' | ' + str(lista[2]))
    print('\t--------------')
    print('\t | ' + str(lista[3]) + ' | ' + str(lista[4]) + ' | ' + str(lista[5]))
    print('\t--------------')
    print('\t | ' + str(lista[6]) + ' | ' + str(lista[7]) + ' | ' + str(lista[8]))
    print('\t--------------')
    
def movimiento(lista,jugador):
    while True:
        movida = input(jugador + ': ¿Cuál sera tu movimiento?: ')
        try:
            movida = int(movida)
            if movida > 0 and movida < 10:
                if lista[movida-1] == '_':
                    lista[movida-1] = jugador
                    break
                else:
                    print('Este lugar ya está ocupado')
            else:
                print('Este movimiento no es válido. Intenta otra vez.')
        except:
            print('Escribe un movimiento válido (1-9)')
            
def ganador(lista,jugador):
    return ((lista[0] == jugador and lista[1] == jugador and lista[2] == jugador) or
            (lista[0] == jugador and lista[4] == jugador and lista[8] == jugador) or
            (lista[2] == jugador and lista[4] == jugador and lista[6] == jugador) or
            (lista[3] == jugador and lista[4] == jugador and lista[5] == jugador) or
            (lista[6] == jugador and lista[7] == jugador and lista[8] == jugador) or
            (lista[0] == jugador and lista[3] == jugador and lista[6] == jugador) or
            (lista[1] == jugador and lista[4] == jugador and lista[7] == jugador) or
            (lista[2] == jugador and lista[5] == jugador and lista[8] == jugador))

while True:
    
    #Imprime los tableros
    tablero(nums_juego)
    print()
    tablero(c_vacios)

    # Empieza Turno Jugador 1
    movimiento(c_vacios,jugador_1)
    
    # Imprime los tableros otra vez después del movimiento 
    tablero(nums_juego)
    print()
    tablero(c_vacios)
    
    # Verifica si Jugador 1 Gana
    victoria = ganador(c_vacios,jugador_1)
    if victoria:
        print('La victoria es para X')
        break
    elif '_' not in c_vacios:
        print('Empate')
        break
        
    # Turno Jugador 2
    movimiento(c_vacios,jugador_2)
    
    # Verifica si Jugador 2 Gana
    victoria = ganador(c_vacios,jugador_2)
    if victoria:
        print('La victoria es para O')
        break
    
        