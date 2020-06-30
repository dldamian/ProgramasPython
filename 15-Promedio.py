print('Calculadora de Promedio\n')

nombre = input('Escribe tu nombre: ').title()
while True:
    num_materias = input('¿Cuántas materias te gustaría ingresar?: ')
    try:
        num_materias = int(num_materias)
        break
    except:
        print('Solo números enteros')
    
calificaciones = []
for n in range(num_materias):
    while True:
        calif = input('Ingresa una calififación (' + str(n+1) + '/' + str(num_materias) + ') : ')
        try:
            calif = int(calif)
            if calif >= 0 and calif < 101:
                calificaciones.append(calif)
                break
            else:
                print('Solo valores del 0-100')
        except:
            print('Solo números enteros')
            
calificaciones.sort(reverse=True)

print('\nEstas son tus calificaciones de mayor a menor:')
for c in calificaciones:
    print('\t' + str(c))
    
print('\n' + nombre + ', este es tu resumen:')
print('\tTotal de materias: ' + str(len(calificaciones)))
print('\tCalificación más alta: ' + str(calificaciones[0]))
print('\tCalificación más baja: ' + str(calificaciones[-1]))

promedio = round(sum(calificaciones) / len(calificaciones),2)
    
print('\tPromedio: ' + str(promedio))


while True:
    promedio_deseado = input('\n¿Cuál es tu promedio deseado?: ')
    try:
        promedio_deseado = float(promedio_deseado)
        if promedio_deseado > 0 and promedio_deseado < 101:
            calif_deseado = promedio_deseado*(len(calificaciones)+1) - sum(calificaciones)
            if calif_deseado > 101:
                print('Para conseguir tu promedio deseado de ' + str(promedio_deseado) + ' necesitarías ' + str(calif_deseado) + ' en tu próxima calificación, lo cúal sería imposible. Lo sentimos :(')
                break
            else:
                print('Para conseguir tu promedio deseado de ' + str(promedio_deseado) + ' necesitas ' + str(calif_deseado) + ' en tu próxima calificación :) ')
                break
        else:
            print('Ingresa solo valores de 0-100')
            
    except:
        print('Ingresa solo números')
        

####
calificaciones_falsas = calificaciones.copy()
print('\nVeremos cómo sería tu promedio si tuvieras una peor o mejor calificación en una materia')
while True:
    cambiar_calif = input('Ingresa la calificación que deseas cambiar: ')
    try:
        cambiar_calif = int(cambiar_calif)
        if cambiar_calif in calificaciones_falsas:
            while True:
                nueva_calif = input('Escribe la nueva calificación: ')
                try:
                    nueva_calif = int(nueva_calif)
                    calificaciones_falsas.remove(cambiar_calif)
                    calificaciones_falsas.append(nueva_calif)
                    break
                except:
                    print('Solo números enteros')
        else:
            print('Esa calificación no está en tu lista')
        break
    except:
        print('Esa calificación no está en tu lista')

calificaciones_falsas.sort(reverse=True)

print('\nEstas son tus calificaciones de mayor a menor:')
for c in calificaciones_falsas:
    print('\t' + str(c))
    
print('\n' + nombre + ', este es tu resumen:')
print('\tTotal de materias: ' + str(len(calificaciones_falsas)))
print('\tCalificación más alta: ' + str(calificaciones_falsas[0]))
print('\tCalificación más baja: ' + str(calificaciones_falsas[-1]))

    
promedio2 = round(sum(calificaciones_falsas) / len(calificaciones_falsas),2)
print('\tPromedio: ' + str(round(promedio2,2)))


diferencia = promedio-promedio2
print('\nTu nuevo promedio sería de ' + str(promedio2) + ', comparado con tu promedio original de ' + str(round(promedio,2)))
print('Esa es una diferencia de ' + str(round(diferencia*-1,2)))