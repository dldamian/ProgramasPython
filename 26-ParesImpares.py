print('Par o Impar APP\n')
reinicio = True
while reinicio:
    print('Escribe números enteros, cualquier otro valor será ignorado.')
    numeros = input('Escribe una serie de números separados por una coma (,): ').split(',')
    numerosb = []
    for num in numeros:
        try:
            if int(num):
                numerosb.append(num)
        except:
            pass
    
    pares = []
    impares = []
    print('\nResultados:')
    for num in numerosb:
        if (int(num)%2) == 0:
            print('\t' + num.strip() + ' es número par')
            pares.append(int(num))
        else:
            print('\t' + num.strip() + ' es número impar')
            impares.append(int(num))
    
    pares.sort()
    impares.sort()
    
    print('\nLos siguientes: ' + str(len(pares)) + ' números son pares:')
    for num in pares:
        print('\t' + str(num))
    
    print('\nLos siguientes: ' + str(len(impares)) + ' números son impares:')
    for num in impares:
        print('\t' + str(num))
    
    eleccion = input('\n¿Deseas volver a usar la APP? (y/n): ')
    if eleccion == 'n':
        reinicio = False
    
print('Gracias por usar la APP')