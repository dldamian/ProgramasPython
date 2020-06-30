print('Bienvenido al clasificador de Calificaciones')

calificaciones = []

def preguntaCalif(num):
    while True:
        calif = input(f'Escribe tu {num} calificación: ')
        try:
            calif = int(calif)
            if calif >= 0 and calif < 101:
                calificaciones.append(calif)
                break
            else:
                print('Escribe números enteros entre 0 y 100')
        except:
            print('Escribe solo números enteros')

preguntaCalif('primera')
preguntaCalif('segunda')
preguntaCalif('tercera')
preguntaCalif('cuarta')

print(f'\nTus calificaciones son: {calificaciones}')
print('\nTus 2 calificaciones más bajas serán eliminadas:')
calificaciones.sort()
calif_fuera = calificaciones.pop(0)
print(f'Calificación eliminada: {calif_fuera}')
calif_fuera = calificaciones.pop(0)
print(f'Calificación eliminada: {calif_fuera}')

print(f'\nTus calificaciones restantes son: {calificaciones}')
print(f'¡Bien hecho! tu calificación más alta es {calificaciones[1]}')