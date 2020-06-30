print('Bienvenido a Factores de Números APP')

reinicio = True
while reinicio:
    factor = input('¿De qué número deseas saber sus factores?: ')
    try:
        factor = int(factor)
        if factor > 0:
            num = 1
            print('\nEstos son sus factores: ')
            lista = []
            while num <= factor:
                if (factor%num) == 0:
                    print(num)
                    lista.append(num)
                num +=1
            print('\nEste es el resumen: ')
            for i in range(int(len(lista)/2)):
                print(str(lista[i]) + '*' + str(lista[-i-1]) + ' = ' + str(factor))
            
            loop = input('¿Deseas continuar? (y/n): ').lower()
            if loop == 'n':
                reinicio = False
                
        else:
            print('Ingresa números enteros o mayores a 0')
    except:
        print('Respuesta no válida. Ingresa solo números enteros.')

print('\nGracias por usar la APP.')