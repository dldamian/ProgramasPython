import random

print('Bienvenido a la Loteria APP')


iniciador = True
while iniciador:
    # Conseguiremos el valor de las blancas
    while True:
        blancas = input('¿Hasta que número te gustaría que llegaran las 5 bolas blancas? (Normalmente hasta el 69): ')
        try:
            blancas = int(blancas)
            if blancas <= 5:
                print('El valor minimo es de 6')
            elif blancas > 69:
                print('El valor máximo es de 69')
            else:
                break
        except:
            print('Solo números enteros')
    
    # Conseguiremos el valor de la bola roja
    while True:
        roja = input('¿Hasta que número te gustaría que llegaran la bola roja? (Normalmente hasta el 26): ')
        try:
            roja = int(roja)
            if roja > 26:
                print('El valor máximo es de 26')
            elif roja < 1:
                print('El valor mínimo es de 1')
            else:
                break
        except:
            print('Solo números enteros')
    
    # Preguntamos cuántos tickets compraremos
    while True:
        tickets = input('¿Cuántos tickets te gustaría comprar?: ')
        try:
            tickets = int(tickets)
            break
        except:
            print('Solo números enteros')
    
    
    # Generaremos los números ganadores
    ganador = []
    while len(ganador) < 5:
        nblanca = random.randint(1,blancas)
        if nblanca not in ganador:
            ganador.append(nblanca)
    ganador.sort()
    nroja = random.randint(1,roja)
    ganador.append(nroja)
    
    
    # Mensaje de bienvenida
    print('\n-----Bienvenido a la Lotería-----')
    print('Los números ganadores son: ' + str(ganador))
    input('Presiona ENTER para ver los tickets que has comprado')
    
    # Loop para ver los tickets comprados
    lista_comprados = []
    while True:
        ticket = 1
        activo = True
        while activo and ticket <= tickets:
            ticket_comprado = []
            while len(ticket_comprado) < 5:
                nblanca = random.randint(1,blancas)
                if nblanca not in ticket_comprado:
                    ticket_comprado.append(nblanca)
            ticket_comprado.sort()
            nroja = random.randint(1,roja)
            ticket_comprado.append(nroja)
            # Si el ticket comprado no está en la lista de comprados, se añade y se suma un ticket
            if ticket_comprado not in lista_comprados:
                lista_comprados.append(ticket_comprado)
                ticket +=1
                print(ticket_comprado)
            
            # Si el ticket comprado es el mismo que el ticket ganador, se tiene el loop
            if ticket_comprado == ganador:
                print('El ticket de arriba es ganador')
                activo = False
        
        # Sale del loop, y si ya salió el ticket ganador, rompe el While
        if ticket_comprado == ganador:
            print('Se acabo el juego, tuviste que comprar ' + str(len(lista_comprados)) + ' tickets para ganar.')
            break
        
        
        # Sale del loop y si aún NO sale el ticket ganador, pregunta para seguir comprado tickets
        print('\nLos números ganadores siguen siendo: ' + str(ganador))    
        seguir = input('¿Deseas comprar otros ' + str(tickets) + ' tickets?: (Y/N)?: ').lower()
        if seguir == 'n':
            print('Compraste ' + str(len(lista_comprados)) + ' tickets y ni así ganaste')
            break
    
    # Si se sale del loop de comprar tickets, pregunta si desea volver a jugar. Reinicia todo
    reinicio = input('\n¿Quieres jugar otra vez? (y/n): ').lower()
    if reinicio == 'n':
        iniciador = False
    
print('Gracias por jugar')