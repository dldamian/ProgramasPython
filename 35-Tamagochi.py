import random

print('Tamagochi APP\n')

class Tamagochi():
    
    #Iniciamos self
    def __init__(self,nombre,dificultad,hambre=0,aburrido=0,cansado=0,sucio=0,comida=2,status=True):
        self.nombre = nombre
        self. hambre = hambre
        self.aburrido = aburrido
        self.cansado = cansado
        self.sucio = sucio
        self.status = status
        self.dificultad = dificultad
        self.comida = 2
        
    
    def mostrarInfo(self):
        print('Nombre de la criatura: ' + self.nombre)
        print('Hambriento (1-10): ' + str(self.hambre))
        print('Aburrido (1-10): ' + str(self.aburrido))
        print('Cansado (1-10): ' + str(self.cansado))
        print('Sucio (1-10): ' + str(self.sucio))
        print('\nComida disponible: ' + str(self.comida))
        if self.status:
            print('Status: Despierto')
        else:
            print('Status: Dormiendo...')
        
    
    def actualizarStatus(self):
        if self.dificultad == 1:
            # Si ESTÁ DESPIERTO
            if mitamagochi.status: 
                self.hambre += random.randint(0,1)
                self.aburrido += random.randint(0,1)
                if self.aburrido >= 10:
                    self.aburrido = 10
                    print('Se fue a dormir por estar aburrido...')
                    self.aburrido -= 8
                    self.cansado = 0
                    self.status = False
                self.cansado += random.randint(0,1)
                if self.cansado >= 10:
                    self.cansado = 10
                    print('Se fue a dormir...estaba muy cansado')
                    self.cansado = 0
                    self.status = False
                self.sucio += random.randint(0,1)
            
            #Si NO ESTÁ DESPIERTO
            else:   
                self.hambre += random.randint(0,1)
                self.sucio += random.randint(0,1)
        
        # Actualizar Status NIVEL 2
        elif self.dificultad == 2:
            # Si ESTÁ DESPIERTO
            if mitamagochi.status: 
                if self.hambre < 8:
                    self.hambre += random.randint(0,2)
                else:
                    self.hambre += random.randint(0,1)

                if self.aburrido < 8:
                    self.aburrido += random.randint(0,2)
                else:
                    self.aburrido += random.randint(0,1)
                    if self.aburrido >= 10:
                        self.aburrido = 10
                        print('Se fue a dormir por estar aburrido...')
                        self.aburrido -= 6
                        self.cansado = 0
                        self.status = False
                self.cansado += random.randint(0,2)
                if self.cansado > 10:
                    self.cansado = 10
                    print('Se fue a dormir...estaba muy cansado')
                    self.cansado = 0
                    self.status = False
                if self.sucio < 8:
                    self.sucio += random.randint(0,2)
                    if self.sucio > 10:
                        self.sucio = 10
                else:
                    self.sucio += random.randint(0,1)
            
            #Si NO ESTÁ DESPIERTO
            else:   
                self.hambre += random.randint(0,1)
                self.sucio += random.randint(0,1)
                
        
        # Actualizar Status NIVEL 3
        elif self.dificultad == 3:
            # Si ESTÁ DESPIERTO
            if mitamagochi.status: 
                if self.hambre < 8:
                    self.hambre += random.randint(1,2)
                else:
                    self.hambre += random.randint(0,1)

                if self.aburrido < 8:
                    self.aburrido += random.randint(0,2)
                else:
                    self.aburrido += random.randint(0,1)
                    if self.aburrido >= 10:
                        self.aburrido = 10
                        print('Se fue a dormir por estar aburrido...')
                        self.aburrido -= 5
                        self.cansado = 0
                        self.status = False
                self.cansado += random.randint(0,2)
                if self.cansado > 10:
                    self.cansado = 10
                    print('Se fue a dormir...estaba muy cansado')
                    self.cansado = 0
                    self.status = False
                if self.sucio < 8:
                    self.sucio += random.randint(0,2)
                    if self.sucio > 10:
                        self.sucio = 10
                else:
                    self.sucio += random.randint(0,1)
            
            #Si NO ESTÁ DESPIERTO
            else:   
                self.hambre += random.randint(0,1)
                self.sucio += random.randint(0,1)
                
                
        elif self.dificultad == 4:
            # Si ESTÁ DESPIERTO
            if mitamagochi.status: 
                if self.hambre < 8:
                    self.hambre += random.randint(1,2)
                else:
                    self.hambre += random.randint(0,1)

                if self.aburrido < 8:
                    self.aburrido += random.randint(1,2)
                else:
                    self.aburrido += random.randint(0,1)
                    if self.aburrido >= 10:
                        self.aburrido = 10
                        print('Se fue a dormir por estar aburrido...')
                        self.aburrido -= 4
                        self.cansado = 0
                        self.status = False
                self.cansado += random.randint(0,2)
                if self.cansado > 10:
                    self.cansado = 10
                    print('Se fue a dormir...estaba muy cansado')
                    self.cansado = 0
                    self.status = False
                if self.sucio < 8:
                    self.sucio += random.randint(1,2)
                    if self.sucio > 10:
                        self.sucio = 10
                else:
                    self.sucio += random.randint(0,1)
            
            #Si NO ESTÁ DESPIERTO
            else:   
                self.hambre += random.randint(0,1)
                self.sucio += random.randint(0,1)
                
                
        # Status NIVEL 5
        else:
           # Si ESTÁ DESPIERTO
            if mitamagochi.status: 
                if self.hambre < 8:
                    self.hambre += random.randint(1,2)
                else:
                    self.hambre += random.randint(0,1)

                if self.aburrido < 8:
                    self.aburrido += random.randint(1,2)
                else:
                    self.aburrido += random.randint(0,1)
                    if self.aburrido >= 10:
                        self.aburrido = 10
                        print('Se fue a dormir por estar aburrido...')
                        self.aburrido -= 4
                        self.cansado = 0
                        self.status = False
                self.cansado += random.randint(1,2)
                if self.cansado > 10:
                    self.cansado = 10
                    print('Se fue a dormir...estaba muy cansado')
                    self.cansado = 0
                    self.status = False
                if self.sucio < 8:
                    self.sucio += random.randint(1,2)
                    if self.sucio > 10:
                        self.sucio = 10
                else:
                    self.sucio += random.randint(0,1)
            
            #Si NO ESTÁ DESPIERTO
            else:   
                self.hambre += random.randint(0,1)
                self.sucio += random.randint(0,1)
    
    def comer(self):
        self.comida -= 1
        if self.comida >= 1:
            if self.dificultad == 1:
                self.hambre -= random.randint(1,5)
                if self.hambre < 0:
                    self.hambre = 0
            elif self.dificultad == 2:
                self.hambre -= random.randint(1,4)
                if self.hambre < 0:
                    self.hambre = 0
            elif self.dificultad == 3:
                self.hambre -= random.randint(1,3)
                if self.hambre < 0:
                    self.hambre = 0
            elif self.dificultad == 4:
                self.hambre -= random.randint(1,2)
                if self.hambre < 0:
                    self.hambre = 0
            else:
                self.hambre -= random.randint(1,2)
                if self.hambre < 0:
                    self.hambre = 0
            print(self.nombre + ' ha comido')
        else:
            print('No puedes darle de comer a ' + self.nombre + ', no tienes comida en tu inventario')
            self.comida = 0
                
                
    def jugar(self):
        num = random.randint(1,3)
        print(self.nombre + ' está pensando en un número del 1 al 3...')
        chance = input('¿Qué número será?: ')
        if chance == str(num):
            print('¡Adivinaste! ¡Qué divertido')
            self.aburrido -= 3
            if self.aburrido < 0:
                self.aburrido = 0
        else:
            print('No adivinaste...')
            self.aburrido -= 1
            if self.aburrido < 0:
                self.aburrido = 0
            
    def domir(self):
        self.cansado = 0
        self.aburrido -= 2
        print(self.nombre + ' ha dormido')
        
        if self.cansado < 0:
            self.cansado = 0
        if self.aburrido < 0:
            self.aburrido = 0
        
    def despertar(self):
        num = random.randint(1,2)
        if num == 1:
            print('¡Despertó!')
            self.status = True
        else:
            print('No despierta...')
            self.aburrido -= 1
            if self.aburrido < 0:
                self.aburrido = 0
            self.status = False
            
    def limpiar(self):
        if self.dificultad == 1:
            self.sucio = 0
        elif self.dificultad == 2:
            self.sucio -= random.randint(1,8)
            if self.sucio < 0:
                self.sucio = 0
        elif self.dificultad == 3:
            self.sucio -= random.randint(1,6)
            if self.sucio < 0:
                self.sucio = 0
        elif self.dificultad == 4:
            self.sucio -= random.randint(1,5)
            if self.sucio < 0:
                self.sucio = 0
        else:
            self.sucio -= random.randint(1,4)
            if self.sucio < 0:
                self.sucio = 0
        print(self.nombre + ' se ha bañado')
                
    def buscarComida(self):
        if self.dificultad == 1:
            self.comida += random.randint(1,10)
        elif self.dificultad == 2:
            self.comida += random.randint(1,8)
        elif self.dificultad == 3:
            self.comida += random.randint(1,6)
        elif self.dificultad == 4:
            self.comida += random.randint(1,5)
        else:
            self.comida += random.randint(1,4)
        print(self.nombre + ' ha encontrado algo de comida...')
        
    def vivo(self):
        if self.hambre == 10:
            print(self.nombre + ' murió de hambre...')
            return False
        elif self.sucio == 10:
            print(self.nombre + ' murió por una infección porque no lo bañaste...')
            return False
        else:
            return True
        

while True:
    tamagochi = input('Escribe un nombre para tu Tamagochi: ').title()
    while True:
        level = input('Escribe el nivel de dificultad (1-5): ')
        try:
            level = int(level)
            if level == 1 or level == 2 or level == 3 or level == 4 or level == 5:
                break
            else:
                print('No es una respuesta válida')
        except:
            print('Respuesta no válida')
            
            
    mitamagochi = Tamagochi(tamagochi,level)

    rondas = 1
    print(mitamagochi.status)
    while mitamagochi.vivo():


        print('\n---------' + 'Ronda ' + str(rondas) + '---------')
        mitamagochi.mostrarInfo()

        
        
        if mitamagochi.status:
            while True:
                print('\n¿Qué quieres hacer?')
                print('1) Comer\n2) Jugar\n3) Dormir\n4) Bañarse\n5) Buscar comida')
                eleccion = input('Escribe tu respuesta: ')
                try:
                    eleccion = int(eleccion)
                    if eleccion == 1 or eleccion == 2 or eleccion == 3 or eleccion == 4 or eleccion == 5:
                        break
                    else:
                        print('Respuesta no válida')
                except:
                    print('Respuesta no válida')
        else:
            eleccion = input('\nPresina ENTER para tratar de despertarlo...')


        if eleccion == 1:
            mitamagochi.comer()
        elif eleccion == 2:
            mitamagochi.jugar()
        elif eleccion == 3:
            mitamagochi.domir()
        elif eleccion == 4:
            mitamagochi.limpiar()
        elif eleccion ==5 :
            mitamagochi.buscarComida()
        else:
            mitamagochi.despertar()
        
        
        input('Presiona ENTER para continuar')
        
        mitamagochi.actualizarStatus()
        rondas += 1
        
    print('Sobreviviste ' + str(rondas) + ' rondas')
    
    jugar = input('¿Deseas jugar otra vez?: (y/n): ')
    if jugar == 'n':
        break