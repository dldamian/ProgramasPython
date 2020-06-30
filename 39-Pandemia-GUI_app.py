import random
import math
import tkinter

class Simulacion():
    
    '''Aquí se obtienen las variables que se necesitan para hacer la simulación'''
    
    def __init__(self):
        
        # El día actual de la simulación, este se irá incrementando durante loops del programa
        self.num_dia = 1
        
        # Se pide saber la población total y se guarda en variable "poblacion_total"
        print('Para hacer la simulación, se necesita saber el tamaño de la población')
        while True:
            self.poblacion_total = input('Escribe la población total: ')
            try:
                self.poblacion_total = int(self.poblacion_total)
                self.raiz = math.sqrt(self.poblacion_total)
                if int(self.raiz+0.5)**2 != self.poblacion_total:
                    self.tablero = int(self.raiz)
                    self.poblacion_total = self.tablero**2
                    print('Se ha redondeado la población a ' + str(self.poblacion_total) + ' por razones de visualización')
                    break
                else:
                    self.tablero = int(self.raiz)
                    break
            except:
                print('Escribe solo números enteros')
                
        
        # Se pude saber el porcentaje de la poblacion infectada inicialmente y se almacena
        # en variable "poblacion_infectada"
        print('\nPara hacer la simulación, se necesita saber el porcentaje de la población inicialmente infectada')
        while True:
            self.poblacion_infectada = input('Escribe el porcentaje de la población infecta inicial (0-100): ')
            try:
                self.poblacion_infectada = float(self.poblacion_infectada)
                if self.poblacion_infectada >= 0 and self.poblacion_infectada <= 100:
                    break
                else:
                    print('Escribe un porcentaje de 0 a 100')
            except:
                print('Escribe solo números enteros')
        self.poblacion_infectada = self.poblacion_infectada/100
        
        
        # Se pide saber el porcentaje de probabilidad de que alguien se contagie
        # y se guarda en variable "probabilidad_contagio"
        print('\nPara hacer la simulación, se necesita saber el porcentaje de probabilidad de que alguien se contagie')
        while True:
            self.probabilidad_contagio = input('Escribe la probabilidad de contagio (1-100): ')
            try:
                self.probabilidad_contagio = float(self.probabilidad_contagio)
                if self.probabilidad_contagio >= 0 and self.probabilidad_contagio <= 100:
                    break
                else:
                    print('Escribe un porcentaje de 0 a 100')
            except:
                print('Escribe solo números enteros')        
        
        
        # Se pide la durabilidad del virus y se guarda en variable "durabilidad_virus"
        print('\nPara hacer la simulación, se necesita saber la durabilidad del virus en días')
        while True:
            self.durabilidad_virus = input('Escribe la durabilidad del virus en días: ')
            try:
                self.durabilidad_virus = int(self.durabilidad_virus)
                break
            except:
                print('Escribe solo números enteros')
                
        
        # Se pide el porcentaje de mortalidad y se guarda en variable "mortalidad"
        print('\nPara hacer la simulación, se necesita saber el porcentaje de mortalidad')
        while True:
            self.mortalidad = input('Escribe el porcentaje de mortalidad (1-100): ')
            try:
                self.mortalidad = float(self.mortalidad)
                if self.mortalidad >= 0 and self.mortalidad <= 100:
                    break
                else:
                    print('Escribe un porcentaje de 0 a 100')
            except:
                print('Escribe solo números enteros')
        
        
        # Se pide los días que durará la simulación y se guarda en variable "duracion_simulacion"
        print('\nPara hacer la simulación, se necesita saber la duración de la simulación el días')
        while True:
            self.duracion_simulacion = input('Escribe la duración de la simulación: ')
            try:
                self.duracion_simulacion = int(self.duracion_simulacion)
                break
            except:
                print('Escribe solo números enteros')

class Persona():
    
    '''Se crea una persona y funciones para curarla o matarla según sea el caso'''
    
    def __init__(self):
        
        # En principio una persona NO está infectada y NO esta muerta (FALSE en ambas variables)
        # Los días de infectada es 0 y se irán sumando +1 en loops según sea el caso
        self.esta_infectada = False
        self.esta_muerta = False
        self.dias_infectada = 0
        
        
    def infectada(self,simulacion):
        
        # Si la probabilidad es mayor a la probabilidad_contagio (variable de la clase SIMULACIÓN),
        # entonces la persona estará contagiada y la variable self.esta_infectada pasa a ser True
        if random.randint(0, 100) < simulacion.probabilidad_contagio:
            self.esta_infectada = True
            
    def recuperada(self):
        # Si una persona se recupera, la variable self.esta_infectada pasa a ser FALSE otra vez
        # y los días de infectada pasan a ser 0 otra vez (self.dias_infectada = 0)
        self.esta_infectada = False
        self.dias_infectada = 0
        
    def muerta(self):
        # Si la persona muere, la variable self.esta_muerta pasa a ser TRUE
        self.esta_muerta = True
        
        
    def actualizar(self,simulacion):
        
        # Se actualiza a la persona para contagiarla (o no), o ver si ha muerto (o no)
    
        # Si la persona NO está muerta:
        if not self.esta_muerta:
            #Si la persona NO esta muerta, pero está infectada, se suma +1 a los días_infectada
            if self.esta_infectada:
                self.dias_infectada += 1
                # Si la persona ESTÁ INFECTADA, tiene probabilidades de morir, esa probabilidad
                # se crea en la variable "probabilidad" del 1 al 100
                # Si la probabilidad es menor a la mortalidad, esa persona MUERE
                if random.randint(0, 100) < simulacion.mortalidad:
                    self.muerta()
                # Si los días_infectada de la persona es igual a la durabilidad_virus,
                # se presume que se ha recuperado y se llama al metodo self.recuperada()
                elif self.dias_infectada == simulacion.durabilidad_virus:
                    self.recuperada()
    


class Poblacion():
    
    '''Aquí se creará una población con objetos Personas()'''
    
    def __init__(self,simulacion):
        
        # Se crea una lista vacia donde se almacenarán las personas creadas
        self.poblacion = []
            
        for x in range(simulacion.tablero):
            fila = []
            for x in range(simulacion.tablero):
                persona = Persona()
                fila.append(persona)
            
            self.poblacion.append(fila)
            
    def infeccion_inicial(self,simulacion):
        '''Después de crear personas y almacenarlos en la lista self.población
            se infectarán aleatoriamente a X número de personas'''
        
        # Se contagiarán solo el número de personas que se dijo en la variable "poblacion_infectada"
        # del clase Simulación
        contador_infectados = int(round(simulacion.poblacion_total * simulacion.poblacion_infectada,0))
        
        infecciones = 0
        
        while infecciones < contador_infectados:
            x = random.randint(0,simulacion.tablero-1)
            y = random.randint(0,simulacion.tablero-1)
            if not self.poblacion[x][y].esta_infectada:
                self.poblacion[x][y].esta_infectada = True
                self.poblacion[x][y].dias_infectada += 1
                infecciones += 1
        
        
    def esparcir_virus(self,simulacion):
        '''Se esparce el virus cada que un loop llame a esta función'''
                        
        for x in range(simulacion.tablero):
            for y in range(simulacion.tablero):
                if not self.poblacion[x][y].esta_muerta:
                    if x == 0:
                        if y == 0:
                            if self.poblacion[x+1][y].esta_infectada or self.poblacion[x][y+1].esta_infectada:
                                self.poblacion[x][y].infectada(simulacion)
                        elif y == simulacion.tablero-1:
                            if self.poblacion[x][y-1].esta_infectada or self.poblacion[x+1][y].esta_infectada:
                                self.poblacion[x][y].infectada(simulacion)
                        else:
                            if self.poblacion[x][y+1].esta_infectada or self.poblacion[x][y-1].esta_infectada or self.poblacion[x+1][y].esta_infectada:
                                self.poblacion[x][y].infectada(simulacion)
                    elif x == simulacion.tablero-1:
                        if y == 0:
                            if self.poblacion[x][y+1].esta_infectada or self.poblacion[x-1][y].esta_infectada:
                                self.poblacion[x][y].infectada(simulacion)
                        elif y == simulacion.tablero-1:
                            if self.poblacion[x][y-1].esta_infectada or self.poblacion[x-1][y].esta_infectada:
                                self.poblacion[x][y].infectada(simulacion)
                        else:
                            if self.poblacion[x][y-1].esta_infectada or self.poblacion[x][y+1].esta_infectada or self.poblacion[x-1][y].esta_infectada:
                                self.poblacion[x][y].infectada(simulacion)
                    else:
                        if y == 0:
                            if self.poblacion[x][y+1].esta_infectada or self.poblacion[x+1][y].esta_infectada or self.poblacion[x-1][y].esta_infectada:
                                self.poblacion[x][y].infectada(simulacion)
                        elif y == simulacion.tablero-1:
                            if self.poblacion[x][y-1].esta_infectada or self.poblacion[x+1][y].esta_infectada or self.poblacion[x-1][y].esta_infectada:
                                self.poblacion[x][y].infectada(simulacion)
                        else:
                            if self.poblacion[x][y+1].esta_infectada or self.poblacion[x][y-1].esta_infectada or self.poblacion[x-1][y].esta_infectada or self.poblacion[x+1][y].esta_infectada:
                                self.poblacion[x][y].infectada(simulacion)
                        
    def actualizar(self,simulacion):
        # Se actualiza el número de día del loop +1
        simulacion.num_dia += 1
        
        # A cada persona de la lista self.poblacion se actualiza su estado
        for fila in self.poblacion:
            for persona in fila:
                persona.actualizar(simulacion)
            
    def mostrar_estadisticas(self,simulacion):
        total_infectados = 0
        total_muertos = 0
        
        for fila in self.poblacion:
            for persona in fila:
                if persona.esta_infectada:
                    total_infectados += 1
                    if persona.esta_muerta:
                        total_muertos += 1
                    
        porcentaje_infectados = (total_infectados*100) / simulacion.poblacion_total
        porcentaje_infectados = round(porcentaje_infectados,2)
        
        porcentaje_muertos = (total_muertos*100) / simulacion.poblacion_total
        porcentaje_muertos = round(porcentaje_muertos,2)
        
        print('Día: ' + str(simulacion.num_dia))
        print('Población: ' + str(simulacion.poblacion_total) + ' personas')
        print('Personas infectadas: ' + str(porcentaje_infectados) + '%')
        print('Personas muertas: ' + str(porcentaje_muertos) + '%')
        print('Total infectados: ' + str(total_infectados))
        print('Total muertes: ' + str(total_muertos))
        
    
def graficos(simulacion,poblacion,canvas):
    
    cuadrado = 600 // simulacion.tablero
    
    for i in range(simulacion.tablero):
        y = i*cuadrado
        for j in range(simulacion.tablero):
            x = j*cuadrado
            if poblacion.poblacion[i][j].esta_muerta:
                canvas.create_rectangle(x, y, x+cuadrado, y+cuadrado, fill="red")
            else:
                if poblacion.poblacion[i][j].esta_infectada:
                    canvas.create_rectangle(x, y, x+cuadrado, y+cuadrado, fill="Yellow")
                else:
                    canvas.create_rectangle(x, y, x+cuadrado, y+cuadrado, fill="green")
    
            

print('PANDEMIA APP')

# Se hace la simulación (se obtienen las variables iniciales)
simulacion = Simulacion()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

ventana = tkinter.Tk()
ventana.title('Simulación de Epidemia')
canvas = tkinter.Canvas(ventana, width=WINDOW_WIDTH,height=WINDOW_HEIGHT, bg="lightblue")
canvas.pack(side=tkinter.LEFT)

# Se crea una población y se le meten los valores de la simulación
poblacion = Poblacion(simulacion)

# Se infectan a las primeras personas
poblacion.infeccion_inicial(simulacion)
# Muestra las estadísticas y gráifoc del día 1
poblacion.mostrar_estadisticas(simulacion)

# Para continuar el usuario debe presionar ENTER
input('\nPresiona ENTER para hacer la simulacion del día siguiente\n')

# Inicia LOOP por cada día que se quiera hacer la simulación
for i in range(1,simulacion.duracion_simulacion):
    print('----------------------------------------------------------')
    
    # Esparce el virus nuevamente
    poblacion.esparcir_virus(simulacion)
    # Actualiza el estado de cada persona de la población
    poblacion.actualizar(simulacion)
    # Muestra estadísticas y gráfico de la simulación
    poblacion.mostrar_estadisticas(simulacion)
    
    graficos(simulacion,poblacion,canvas)
    ventana.update()
    
    if i != simulacion.duracion_simulacion-1:
        canvas.delete('all')
    
    

print('\nTermino la simulación')
