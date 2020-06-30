import random

print('Bienvenido a Adivina mi Número')

nombre = input('¡Hola! ¿Cuál es tu nombre?: ').title()
print('Bienvenido ' + nombre + ', estoy pensando en un número del 1-20\n')

numero_azar = random.randint(1,20)
intentos = 1

while True:
    if intentos <= 5:
        numero = input('Adivina el número: ')
        try:
            numero = int(numero)
            if numero <= 20:
                if numero < numero_azar:
                    print('Muy bajo')
                elif numero > numero_azar:
                    print('Muy alto')
                else:
                    print('\n¡Adivinaste! El número que estaba pensando era ' + str(numero_azar))
                    print('Te tomó ' + str(intentos) + ' intentos adivinar')
                    break
                intentos +=1
            else:
                print('Ingresa solo números menores o igual a 20')
        except:
            print('Ingresa solo números')
    else:
        print('\nSe acabaron las oportunidades, el número era ' + str(numero_azar))
        break
