import random

print('Bienvenido al Dado APP')

def dado(lados,tiros):
    print('\nTiraste ' + str(tiros) + ' tiros el dado de ' + str(lados) + ' lados')
    print('\nEstos son tus resultados:')
    total = 0
    for tiro in range(1,tiros+1):
        x = random.randint(1,lados)
        print('\t\t' + str(x))
        total = total + x
    print('La suma de todos los tiros es ' + str(total))
    

def preguntaLados():
    while True:
        lados = input('\n¿Cuántos lados quieres que tenga tu dado?: ')
        try:
            lados = int(lados)
            break
        except:
            print('Escribe solo números enteros')
    return lados

def preguntaTiros():
    while True:
        tiros = input('¿Cuántos tiros quieres que hacer?: ')
        try:
            tiros = int(tiros)
            break
        except:
            print('Escribe solo números enteros')
    return tiros
    
while True:
    
    lados = preguntaLados()
    tiros = preguntaTiros()
            
    dado(lados,tiros)
    
    pregunta = input('\nQuieres volver a jugar? (y/n): ').lower()
    if pregunta == 'n':
        break

    
print('Gracias por jugar')