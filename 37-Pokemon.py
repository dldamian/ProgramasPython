import random
import time

class Pokemon():
    
    # TODOS los POKEMONES tendrán nombre, elemento, salud y velocidad
    def __init__(self,nombre,elemento,salud,velocidad):
        self.nombre = nombre
        self.elemento = elemento
        self.salud_max = salud
        self.salud_actual = salud
        self.velocidad = velocidad
        
        # Al momento de crearlos, todos los POKEMONES estarán vivos (TRUE)
        self.esta_vivo = True
        
    # TODOS los POKEMONES tendrán un ataque ligero
    def ataque_ligero(self,enemigo):
        # Se define el valor de daño
        ataque = random.randint(15,25)
        
        #Se imprime el nombre del POKEMON y su MOVIMIENTO LIGERO
        #que está en el index[0] de sus movimientos
        print(self.nombre + ' utilizó ' + self.movimientos[0])
        print('El ataqué tuvo un daño de ' + str(ataque) + ' pts \n')
        
        # Se resta el daño al POKEMON ENEMIGO
        enemigo.salud_actual -= ataque
        
    # TODOS los POKEMONES tendrán un ataque fuerte    
    def ataque_fuerte(self,enemigo):
        
        # Se define el valor de daño
        ataque = random.randint(0,50)
        
        #Se imprime el nombre del POKEMON y su MOVIMIENTO LIGERO
        #que está en el index[1] de sus movimientos
        print(self.nombre + ' utilizó ' + self.movimientos[1])
        
        # Si el ataque es menos a 10, no hace daño
        if ataque < 10:
            print('El ataque falló...no hizo ningún daño\n')
        
        # Si el ataque es igual o mayor a 10, hace daño al enemigo 
        else:
            print('El ataqué tuvo un daño de ' + str(ataque) + ' pts de daño\n')
            enemigo.salud_actual -= ataque
            
    
    # TODOS los POKEMONES pueden recuperar salud utiliazando
    # su moviento en index[2]
    def restaurar_salud(self):
        
        # Se determina cuánta salud recuperará
        recuperacion = random.randint(15,25)
        
        # Se imprime la información: ataqué que usó (index[2])
        # y cuánta salud recuperó
        print(self.nombre + ' utilizó ' + str(self.movimientos[2]))
        print(self.nombre + ' recuperó ' + str(recuperacion) + ' pts de salud\n')
        
        # Se suma la salud recuperada
        self.salud_actual += recuperacion
        
        # Si con la salud recuperata se pasa el límite de su salud máxima,
        # se pone su salud a su salud máxima
        if self.salud_actual > self.salud_max:
            self.salud_actual = self.salud_max
            
    
    # Con esta función se verifica si un pokemon se ha desmayado
    def desmayo(self):
        
        # Si la salud de un pokemon es igual o menor a 0
        # El argumento esta_vivo pasa a ser False
        if self.salud_actual <= 0:
            self.esta_vivo = False
            print('El pokemon ' + self.nombre + ' se ha desmayado...')
            input('Presiona ENTER para continuar')
            
    # Solo muestrá sus estadísticas
    def mostrarEstadisticas(self):
        print('Nombre: ' + self.nombre)
        print('Elemento: ' + self.elemento)
        print('Salud: ' + str(self.salud_actual) + '/' + str(self.salud_max))
        print('Velocidad: ' + str(self.velocidad))
        print()
    
    
class Fuego(Pokemon):
    
    # Hereda los parametros de la clase padre (Pokemon())
    # y se pone una nueva: movimientos, que serán movimientos únicos para pokemones tipo FUEGO
    def __init__(self,nombre,elemento,salud,velocidad):
        super().__init__(nombre,elemento,salud,velocidad)
        
        self.movimientos = ['Rasguño','Embestida','Luz','Explosión']
        
    # Los pokemones tipo FUEGO tienen un ataque único ubicado en movmientos[3]
    def ataqueEspecial(self,enemigo):
        
        # Se imprime el nombre del pokemon y su movimiento
        print(self.nombre + ' utilizó ' + self.movimientos[3])
        
        # Si el enemigo es un tipo de elemento especial,
        # hará más o menor daño
        
        # FUEGO hará más daño a HIERBA
        if enemigo.elemento == 'Hierba':
            ataque = random.randint(35,50)
            print('El ataque es super efectivo ')
        # FUEGO hará poco daño a AGUA
        elif enemigo.elemento == 'Agua':
            ataque = random.randint(5,10)
            print('El ataque no es muy efectivo...')
        # FUEGO hara un daño normal a FUEGO
        else:
            ataque = random.randint(10,30)
            
        # Se imprime el nombre del ataque y los pts de daño efectivos
        print('El ataque fue de ' + str(ataque) + ' pts de daño\n')
        
        # Se resta daño a la salud del enemigo
        enemigo.salud_actual -= ataque
        
    def mostrarMovimientos(self):
        print('Estos son sus movimientos:')
        print(self.movimientos[0] + ': Ataque ligero')
        print(self.movimientos[1] + ': Ataque medio')
        print(self.movimientos[2] + ': Recupera salud')
        print(self.movimientos[3] + ': Ataque fuerte')
        
        
class Agua(Pokemon):
    
    # Hereda los parametros de la clase padre (Pokemon())
    # y se pone una nueva: movimientos, que serán movimientos únicos para pokemones tipo AGUA
    def __init__(self,nombre,elemento,salud,velocidad):
        super().__init__(nombre,elemento,salud,velocidad)
        
        self.movimientos = ['Mordida','Splash','Sumergirse','Tsunami']
        
    # Los pokemones tipo AGUA tienen un ataque único ubicado en movmientos[3]
    def ataqueEspecial(self,enemigo):
        
        # Se imprime nombre del pokemon y nombre desu movimiento
        print(self.nombre + ' utilizó ' + self.movimientos[3])
        
        
        # Si el enemigo es un tipo de elemento especial,
        # hará más o menor daño
        
        # AGUA hará más daño a FUEGO
        if enemigo.elemento == 'Fuego':
            ataque = random.randint(35,50)
            print('El ataque es super efectivo ')
        # AGUA hará menor daño a HIERBA
        elif enemigo.elemento == 'Hierba':
            ataque = random.randint(5,10)
            print('El ataque no es muy efectivo...')
        # AGUA hará un daño normal a AGUA
        else:
            ataque = random.randint(10,30)
            
        # Se imprime el nombre del ataque y los pts de daño efectivos
        # Y se resta salud al enemigo
        print('El ataque fue de ' + str(ataque) + ' pts de daño\n')
        enemigo.salud_actual -= ataque
        
    def mostrarMovimientos(self):
        print('Estos son sus movimientos:')
        print(self.movimientos[0] + ': Ataque ligero')
        print(self.movimientos[1] + ': Ataque medio')
        print(self.movimientos[2] + ': Recupera salud')
        print(self.movimientos[3] + ': Ataque fuerte')
        
class Hierba(Pokemon):
    
    # Hereda los parametros de la clase padre (Pokemon())
    # y se pone una nueva: movimientos, que serán movimientos únicos para pokemones tipo HIERBA
    def __init__(self,nombre,elemento,salud,velocidad):
        super().__init__(nombre,elemento,salud,velocidad)
        
        self.movimientos = ['Viento','Remolino','Enterrarse','Espada de hojas']
        
    
    # Los pokemones tipo HIERBA tienen un ataque único ubicado en movmientos[3]
    def ataqueEspecial(self,enemigo):
        
        # Se imprime nombre del pokemon y nombre desu movimiento
        print(self.nombre + ' utilizó ' + self.movimientos[3])
        
        # Si el enemigo es un tipo de elemento especial,
        # hará más o menor daño
        
        # HIERBA hace más daño a AGUA
        if enemigo.elemento == 'Agua':
            ataque = random.randint(35,50)
            print('El ataque es super efectivo ')
        # HIERBA hace menor daño a FUEGO
        elif enemigo.elemento == 'Fuego':
            ataque = random.randint(5,10)
            print('El ataque no es muy efectivo...')
        # HIERBA hace un daño normal a HIERBA
        else:
            ataque = random.randint(10,30)
            
        # Se imprime el nombre del ataque y los pts de daño efectivos
        # Y se resta salud al enemigo
        print('El ataque fue de ' + str(ataque) + ' pts de daño\n')
        enemigo.salud_actual -= ataque
        
    def mostrarMovimientos(self):
        print('Estos son sus movimientos:')
        print(self.movimientos[0] + ': Ataque ligero')
        print(self.movimientos[1] + ': Ataque medio')
        print(self.movimientos[2] + ': Recupera salud')
        print(self.movimientos[3] + ': Ataque fuerte')
    
        
class Juego():
    
    
    def __init__(self):
        
        self.elementos_pokemon = ['Fuego','Agua','Hierba']
        
        self.nombres_pokemon = ['Bulbasaur','Charmander','Pikachu','Metapod','Caterpie',
                          'Butterfree','Pidgeotto','Rattata','Clefairy','Jigglypuff',
                          'Zubat','Gloom','Meowth','Psyduck','Magneton']
        
        self.batallas_ganadas = 0
        
    def crearPokemon(self):
        
        # Se crean parametros salud, velocidad, elementos y nombre
        salud = random.randint(70,100)
        velocidad = random.randint(1,10)
        elemento = self.elementos_pokemon[random.randint(0,len(self.elementos_pokemon)-1)]
        nombre = self.nombres_pokemon[random.randint(0,len(self.nombres_pokemon)-1)]
        
        # Se crea 1 pokemon de acuerdo al elemento
        if elemento == 'Fuego':
            pokemon = Fuego(nombre,elemento,salud,velocidad)
        elif elemento == 'Agua':
            pokemon = Agua(nombre,elemento,salud,velocidad)
        else:
            pokemon = Hierba(nombre,elemento,salud,velocidad)
            
        # Regresa pokemon que hay que almacenar en una variable para crear objeto
        return pokemon
    
    def escogerPokemon(self):
        
        # Aquí se almacenerán los primeros 3 pokemones del juego
        primeros = []
        
        # Mientras la lista de "primeros" sea menor a 3, se ejecuta
        while len(primeros) < 3:
            
            #Se crea un pokemon al azar con la funcion crearPokemon()
            pokemon = self.crearPokemon()
            # Se pone que es válido en TRUE
            pokemon_valido = True
            
            # Hace loop a la lista "primeros"
            for primero in primeros:
                # Si el nombre o elemento YA ESTÁ en la lista "primeros", regresa
                # pokemon_valido en FALSE
                if primero.nombre == pokemon.nombre or primero.elemento == pokemon.elemento:
                    pokemon_valido = False
            
            # Si después de hacer el LOOP el pokemon es valido
            # se añada a la lista "primeros"
            if pokemon_valido:
                primeros.append(pokemon)
                
        # Imprime los pokemones
        for primero in primeros:
            primero.mostrarEstadisticas()
            primero.mostrarMovimientos
            
        # Inicia la presentación del profesor, aquí inicia el juego
        # y dice los pokemones creados al azar
        print('Soy el Profesor X, estos son los Pokemos disponibles para empezar tu aventura:')
        print('Presiona 1 para escoger a ' + primeros[0].nombre +'\nPresiona 2 para escoger a ' + primeros[1].nombre + '\nPresiona 3 para escoger a ' + primeros[2].nombre)
        
        # Se obliga al usuario a elegir un pokemon del 1 al 3
        while True:
            eleccion = input('¿Qué pokemon eliges?: ')
            try:
                eleccion = int(eleccion)
                if eleccion == 1:
                    pokemon = primeros[0]
                    break
                elif eleccion == 2:
                    pokemon = primeros[1]
                    break
                elif eleccion == 3:
                    pokemon = primeros[2]
                    break
                else:
                    print('Respuesta no válida')
            except:
                print('Respuesta no válida')
                
        # Regresa un pokemon para guardar en una variable
        return pokemon
    
    
    def atacar(self,pokemon):
        
        # Para atacar, debes elegir un movimiento del 1 al 4
        # Aquí solo se imprimen los movimientos disponibles
        print('¿Que movimiento te gustaría hacer?')
        print('Presiona 1 para escoger ' + pokemon.movimientos[0] + '\nPresiona 2 para escoger ' + pokemon.movimientos[1] + '\nPresiona 3 para escoger ' + pokemon.movimientos[2] + '\nPresiona 4 para escoger ' + pokemon.movimientos[3])
        
        # Se obliga al jugador a escoger un movimiento
        while True:
            eleccion = input('¿Qué ataque eliges?: ')
            try:
                eleccion = int(eleccion)
                if eleccion == 1:
                    break
                elif eleccion == 2:
                    break
                elif eleccion == 3:
                    break
                elif eleccion == 4:
                    break
                else:
                    print('Respuesta no válida')
            except:
                print('Respuesta no válida')
                
        # Regresa el NÚMERO del ataque elegido, este número se utliza
        # En la funcion ataqueJugador()
        return eleccion
    
    
    def ataqueJugador(self,ataque,pokemonJugador,pokemonRival):
        
        # Según el ataque elegido, el pokemon del jugador atacará al rival
        if ataque == 1:
            pokemonJugador.ataque_ligero(pokemonRival)
        elif ataque == 2:
            pokemonJugador.ataque_fuerte(pokemonRival)
        elif ataque == 3:
            pokemonJugador.restaurar_salud()
        else:
            pokemonJugador.ataqueEspecial(pokemonRival)
            
        # Después del ataque se verifica que SIGA VIVO o NO
        pokemonRival.desmayo()
        
    def ataqueRival(self,pokemonJugador,pokemonRival):
        # El ataque de rival se selecciona aleatoriamente
        movimiento = random.randint(1,4)
        
        # Segun el movimiento generado aleatoriamente,
        # el pokemon enemigo hará su ataque atacará
        if movimiento == 1:
            pokemonRival.ataque_ligero(pokemonJugador)
        elif movimiento == 2:
            pokemonRival.ataque_fuerte(pokemonJugador)
        elif movimiento == 3:
            pokemonRival.restaurar_salud()
        else:
            pokemonRival.ataqueEspecial(pokemonJugador)
            
        # Después del ataque se verifica que SIGA VIVO o NO
        pokemonJugador.desmayo()
        
    def batalla(self,pokemonJugador,pokemonRival):
        # Se simula la batalla
        
        # Se guarda el ataque elegido por el jugador en esta variable
        eleccion = self.atacar(pokemonJugador)
        
        # Si el pokemon del JUGADOR es más RÁPIDO que POKEMON RIVAL
        # El jugador atacará primero
        if pokemonJugador.velocidad >= pokemonRival.velocidad:
            self.ataqueJugador(eleccion,pokemonJugador,pokemonRival)
            
            # Si después del ataque el POKEMON RIVAL sigue vivo
            # este atacará de vuelta
            if pokemonRival.salud_actual > 0:
                self.ataqueRival(pokemonJugador,pokemonRival)
        
        # Si el pokemon del RIVAL es más RÁPIDO que POKEMON JUGADOR
        # El rival atacará primero
        else:
            self.ataqueRival(pokemonJugador,pokemonRival)
            
            #Si después del ataque, POKEMON JUGADOR sigue vivo, atacamos de vuelta 
            if pokemonJugador.salud_actual > 0:
                self.ataqueJugador(eleccion,pokemonJugador,pokemonRival)
                
                
print('Pokemon APP')
print('''\nEste es tu primer día como entrenador Pokemon, fuiste al laboratorio a escoger
a tu primer compañero de batallas...¿estás listo?''')
input('Presiona ENTER para continuar\n')  

while True:
    # Se inicia el juego
    juego = Juego()
    
    # El usuario debe escoger un pokemon
    pokemonJ = juego.escogerPokemon()
    
    # Se imprime la información del pokemon seleccionado por el usuario
    print('\nEsta es la información de tu pokemon:')
    pokemonJ.mostrarEstadisticas()
    
    # Antes de continuar, el usuario debe presionar ENTER
    input('Presiona ENTER para continuar')
    
    
    # Mientras POKEMON JUGADOR siga vivo:
    while pokemonJ.esta_vivo:
        
        # Se crea un pokemon aleatorio para la PC y se muestran sus detalles
        pokemonPC = juego.crearPokemon()
        print('\n' + pokemonPC.nombre + ' quiere pelear')
        pokemonPC.mostrarEstadisticas()
        
        
        # Mientras POKEMON JUGADOR y POKEMON RIVAL sigan vivos, pelearan:
        while pokemonPC.esta_vivo and pokemonJ.esta_vivo:
            
            # Inicia la batalla
            juego.batalla(pokemonJ,pokemonPC)
            
            # Después de primer intercambio de ataques,
            # se verifica que ambos sigaun vivos para mostrar sus estadisticas actuales
            if pokemonPC.esta_vivo and pokemonJ.esta_vivo:
                pokemonJ.mostrarEstadisticas()
                pokemonPC.mostrarEstadisticas()
                print('---------------------------------------')
                
        # Después del WHILE de la batalla, si el POKEMON JUGADOR sigue vivo,
        # se suma una victoria
        if pokemonJ.esta_vivo:
            juego.batallas_ganadas += 1
            
    
    # Si POKEMON JUGADOR se desmaya, sale del WHILE y se imprimen
    # sus victorias totales
    print('Tu pokemon ' + pokemonJ.nombre + ' se ha desmayado')
    print('Obtuviste ' + str(juego.batallas_ganadas) + ' victorias\n')
    
    pregunta = input('¿Te gustaría jugar otra vez? (y/n): ').lower()
    
    if pregunta == 'n':
        break

        
        
        
        
        
        
        