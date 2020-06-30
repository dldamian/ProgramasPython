print('Bienvenido al clasificador de Calificaciones')
iniciador = True
calificaciones = []

while iniciador:
    calif = input('Escribe tu primera calificación (0-100): ')
    try:
        calif = int(calif)
        if calif >= 0 and calif < 101:
            calificaciones.append(calif)
            while True:
                calif = input('Escribe tu segunda segunda calificación (0-100): ')
                try:
                    calif = int(calif)
                    if calif >= 0 and calif <101:
                        calificaciones.append(calif)
                        while True:
                            calif = input('Escribe tu tercera calificación (0-100): ')
                            try:
                                calif = int(calif)
                                if calif >= 0 and calif < 101:
                                    calificaciones.append(calif)
                                    while True:
                                        calif = input('Escribe tu cuarta calificación (0-100): ')
                                        try:
                                            calif = int(calif)
                                            if calif >= 0 and calif <101:
                                                calificaciones.append(calif)
                                                iniciador = False
                                                break
                                            else:
                                                print('Solo números de 1-100')
                                        except:
                                            print('Escribe solo números')
                                    break
                                else:
                                    print('Solo números de entre 0-100')
                            except:
                                print('Escribe solo números')
                        break
                    else:
                        print('Solo números de entre 0-100')
                except:
                    print('Escribe solo números')
            break
        else:
            print('Solo números de entre 0-100')
    except:
        print('Solo números')
        
print(f'\nTus calificaciones son: {calificaciones}')
print('\nTus 2 calificaciones más bajas serán eliminadas:')
calificaciones.sort()
calif_fuera = calificaciones.pop(0)
print(f'Calificación eliminada: {calif_fuera}')
calif_fuera = calificaciones.pop(0)
print(f'Calificación eliminada: {calif_fuera}')

print(f'\nTus calificaciones restantes son: {calificaciones}')
print(f'¡Bien hecho! tu calificación más alta es {calificaciones[1]}')