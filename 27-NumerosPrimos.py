import math
from time import time

print('Números primos APP')

reinicio = True
while reinicio:
    print('\nEscribe 1 si quieres saber si un númer específico es primo')
    print('Escribe 2 si quieres saber los números primos de un rango específico de números')
    while True:
        opcion = input('Escribe la opción deseada (1/2): ')
        try:
            opcion = int(opcion)
            if opcion == 1:
                break
            elif opcion == 2:
                break
            else:
                print('Escribe solo 1 o 2')
        except:
            print('Escribe solo 1 o 2')
    
    #Verificación de UN número primo dado por usuario
    if opcion == 1:
        while True:
            numoriginal = input('\nEscribe el número que quieras verificar: ')
            try:
                numoriginal = int(numoriginal)
                num = math.factorial(numoriginal-1)
                primo = num + 1
                esprimo = primo % numoriginal
                if esprimo == 0:
                    print(str(numoriginal) + ' es primo')
                else:
                    print(str(numoriginal) + ' no es primo')
                break
            except:
                print('Escribe solo números enteros o mayores a 0')
    #Verificación de números primos por rango de números dados por usuario
    else:
        while True:
            rango1 = input('\nDesde que número quieres verificar: ')
            try:
                rango1 = int(rango1)
                if rango1 > 0:
                    while True:
                        rango2 = input('¿Hasta que número quieres verificar?: ')
                        try:
                            rango2 = int(rango2)
                            if rango2 <= rango1:
                                print('El segundo valor debe ser mayor al primero.')
                            else:
                                print('\nCalculando...')
                                primos = []
                                tiempo = time()
                                for x in range(rango1, rango2+1):
                                    es_primo = True
                                    for num in range(2, x):
                                        if x%num == 0:
                                            es_primo = False
                                            break
                                    if es_primo:
                                        primos.append(x)
                                    
                                
                                duracion = time() - tiempo
                                print("El proceso duró: %0.2f segundos." % duracion)
                                input('Presiona ENTER para ver la lista de primos entre ' + str(rango1) + ' y ' + str(rango2))
                                for primo in primos:
                                    print(primo)
                                break
                        except:
                            print('Ingresa solo números')
                    break
                else:
                    print('Ingresa solo números positivos o mayores a 0')
            except:
                print('Ingresa solo números enteros')
    
    
    
    pregunta = input('¿Quieres volver a usar la APP? (y/n): ').lower()
    if pregunta == 'n':
        reinicio = False

print('\nGracias por usar la app')