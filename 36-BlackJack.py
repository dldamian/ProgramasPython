import random
import time

class BlackJack():
    
    def __init__(self,banco):
        self.banco = banco
        pass

    def barajear(self):
        mazo = []
        #los valores y tipos de cartas
        valor_carta = ['As','2','3','4','5','6','7','8','9','10','J','Q','K']
        tipo_carta = ['Corazones','Espadas','Treboles','Diamantes']
        #Aquí se crean las 52 cartas
        for i in tipo_carta:
            for j in valor_carta:
                mazo.append(j + ' de ' + i)
                
        random.shuffle(mazo)
        return mazo
    
    def repartirJuego(self,mazo):
        cartas_jugador = []
        for i in range(1,3):
            seleccionador = random.randint(1,len(mazo)-1)
            cartas_jugador.append(mazo[seleccionador])
            cartas.pop(seleccionador)
            
        return cartas_jugador
    
    def valorCarta(self,carta):
        valor = carta[0][:1]
        if valor == 'A':
            while True:
                valor = input('¿Cuánto deseas que valga la carta ' + carta + ' ? (1 u 11): ')
                try:
                    valor = int(valor)
                    if valor == 1 or valor == 11:
                        break
                    else:
                        print('No puede valer eso')
                except:
                    print('Escribe 1 u 11')
        elif valor == 'K' or valor == 'Q' or valor == 'J' or valor == '1':
            valor = 10
        else:
            valor = int(carta[0][:1])
                    
        return valor
    
    
    def valorCartaCasa(self,carta):
        azar = random.randint(1,2)
        valor = carta[0][:1]
        if valor == 'A':
            if azar == 1:
                valor = 1
            else:
                valor = 11
        elif valor == 'K' or valor == 'Q' or valor == 'J' or valor == '1':
            valor = 10
        else:
            valor = int(carta[0][:1])
                    
        return valor
    
    
    def sacarCarta(self,mazo,mano):
        num = random.randint(1,len(mazo))
        carta = mazo[num-1]
        mano.append(carta)
        mazo.pop(num-1)
        return carta
    
    
    def ganador(self,totalJugador,totalCasa,dinero):
        if totalJugador > 21:
            print('Perdiste...')
            self.banco -= dinero
        elif totalJugador == 21 and totalCasa == 21:
            print('Empate...nada para nadie')
        elif totalJugador < 21:
            if totalCasa > 21:
                print('Ganaste')
                self.banco += apuesta
            else:
                if totalJugador > totalCasa:
                    print('Ganaste')
                    self.banco += apuesta
                elif totalJugador == totalCasa:
                    print('Empate....nada para nadie')
                else:
                    print('Perdiste')
                    self.banco -= apuesta
        elif totalJugador == 21:
            print('Ganaste')
            self.banco += dinero
        elif totalCasa == 21:
            print('Perdiste')
            self.banco -= dinero
        else:
            print('No se pudo determinar ganador...')


print('BlackJack APP\n')
print('El mínimo para apostar es $20')

while True:
    apostar = input('¿Cuánto quieres tener en tu banco inicial?: ')
    try:
        apostar = float(apostar)
        if apostar >= 20:
            break
        else:
            print('Ingrasa una cantidad mayor a $20')
    except:
        print('Ingresa solo números')
    
juego = BlackJack(apostar)
while juego.banco >= 20:
    
    index_jugador = 0
    index_casa = 0
    
    # Se inicia mostrando el dinero actual
    print('Dinero actual: $' + str(juego.banco))
    
    # Se pide al usuario cuánto apostar, la apuesta mínima debe ser de 20
    while True:
        apuesta = input('¿Cuánto quieres apostar: ')
        try:
            apuesta = float(apuesta)
            if apuesta >= 20:
                break
            else:
                print('Ingrasa una cantidad mayor a $20')
        except:
            print('Ingresa solo números')
    print('Dinero actual: ' + str(juego.banco-apuesta) + '\tApuesta actual: $' + str(apuesta))
    
    
    # Se barajean las cartas
    cartas = juego.barajear()
    
    # Se otorgan 2 cartas al JUGADOR
    mano_j = juego.repartirJuego(cartas)
    valores_cartasj = []
    for x in mano_j:
        x = juego.valorCarta(mano_j[index_jugador])
        valores_cartasj.append(x)
        index_jugador += 1
    
    
    # Se otorgan 2 cartas a la CASA
    mano_casa = juego.repartirJuego(cartas)
    valores_cartasc = []
    for x in mano_j:
        x = juego.valorCartaCasa(mano_casa[index_casa])
        valores_cartasc.append(x)
        index_casa += 1
    
    puntos_casa = sum(valores_cartasc)
    
    # La casa muestra su PRIMERA CARTA
    print('\nLa casa muestra una carta....' + str(mano_casa[0]))
    
    # Se muestra la mano del jugador y se inicia LOOP para sacar cartas las veces que quiera
    print('\nEsta es tu mano:')
    for carta in mano_j:
        print(carta)
    
    puntos_jugador = sum(valores_cartasj)
    print('El total es ' + str(puntos_jugador))
    
    while True:
        eleccion = input('¿Deseas sacar otra carta? (y/n): ')
        if eleccion == 'y':
            juego.sacarCarta(cartas,mano_j)
            nueva_carta = mano_j[index_jugador]
            nueva_carta = juego.valorCarta(nueva_carta)
            valores_cartasj.append(nueva_carta)
            index_jugador += 1
            print('\nEsta es tu mano:')
            for carta in mano_j:
                print(carta)
            puntos_jugador = sum(valores_cartasj)
            print('El total de puntos es de ' + str(puntos_jugador))
        elif eleccion == 'n':
            break
        else:
            print('Elige una opción válida')
    
    # Se saca una carta más a la CASA si sus puntos actuales son <= a 11
    while puntos_casa <= 17:
        juego.sacarCarta(cartas,mano_casa)
        nueva_carta = mano_casa[index_casa]
        nueva_carta = juego.valorCartaCasa(nueva_carta)
        valores_cartasc.append(nueva_carta)
        puntos_casa = sum(valores_cartasc)
        
    print('\nLa casa sacó ' + str(len(mano_casa)) + ' cartas..')
    print('Estás son:')
    for carta in mano_casa:
        print(carta)
        time.sleep(1.5)
    puntos_casa = sum(valores_cartasc)
    print('Los puntos de la casa es ' + str(puntos_casa))
    
    print()
    juego.ganador(puntos_jugador,puntos_casa,apuesta)
    
print('Te quedaste sin banco mínimo para apostar...')
print('El mínimo es $20')
print('Tu banco al terminar la última apuesta es ' + str(juego.banco))
print('Reinicia la APP para volver a jugar')
