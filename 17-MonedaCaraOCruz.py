import random

print('Lanzador de monedas')

print('\nLanzaré las monedas un número determinado de veces')

while True:
    lanzador = input('¿Cuántas veces te gustaría que lanzara la moneda?: ')
    try:
        lanzador = int(lanzador)
        break
    except:
        print('Escribe solo números enteros')
        
while True:
    ver_resultados = input('\n¿Te gustaría ver los resultados? (y/n): ').lower()
    if ver_resultados == 'y':
        cara = 0
        cruz = 0 
        for x in range(lanzador):
            azar = random.randint(1,2)
            if azar == 1:
                cara += 1
                print('CARA')
            else:
                cruz += 1
                print('CRUZ')
            if cara == cruz:
                print('Hubo el mismo número de "CARA" y "CRUZ" al lanzar la moneda ' + str(x+1) + ' veces')
        break    
    elif ver_resultados == 'n':
        print('Okey. Adios')
        break
    else:
        print('Respuesta no válida')
        continue
    break

porcentaje_cara = (cara*100)/lanzador
porcentaje_cruz = (cruz*100)/lanzador


print('\nAquí está un resumen de los resultados: ')
print('\nLado\tContador\tPorcentajes')

print('Cada\t' + str(cara) + '/' + str(lanzador) + '\t\t' + str(porcentaje_cara) + '%')
print('Cada\t' + str(cruz) + '/' + str(lanzador) + '\t\t' + str(porcentaje_cruz) + '%')