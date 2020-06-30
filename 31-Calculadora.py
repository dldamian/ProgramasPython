def numero_uno():
    while True:
        num = input('Ingresa el primer número: ')
        try:
            num = float(num)
            break
        except:
            print('Escribe solo números')
    return num

def numero_dos():
    while True:
        num = input('Ingresa el segundo número: ')
        try:
            num = float(num)
            break
        except:
            print('Escribe solo números')
    return num

def obten_resp():
    while True:
        print('\nOperaciones:')
        print('1 = Suma')
        print('2 = Resta')
        print('3 = Multiplicación')
        print('4 = División')
        respuesta = input('Escribe la operación que deseas hacer: ').lower()
        if respuesta == '1' or respuesta == '2' or respuesta == '3' or respuesta == '4':
            break
        elif respuesta == 'suma' or respuesta == 'resta' or respuesta == 'multiplicacion' or respuesta == 'division':
            break
        else:
            print('Respuesta no válida')
    return respuesta
        
def operacion(respuesta):
    if respuesta == '1' or respuesta == 'suma':
        resultado = valor_1 + valor_2
        print('La suma de ' + str(valor_1) + ' + ' + str(valor_2) + ' es ' + str(resultado))
    elif respuesta == '2' or respuesta == 'resta':
        resultado = valor_1 - valor_2
        print('La resta de ' + str(valor_1) + ' - ' + str(valor_2) + ' es ' + str(resultado))
    elif respuesta == '3' or respuesta == 'multiplicacion':
        resultado = valor_1 * valor_2
        print('La multiplicacion de ' + str(valor_1) + ' * ' + str(valor_2) + ' es ' + str(resultado))
    elif respuesta == '4' or respuesta == 'division':
        if valor_2 == 0:
            print('No se puede dividir entre 0')
            resultado = 'Error'
        else:
            resultado = valor_1 / valor_2
            print('La division de ' + str(valor_1) + ' / ' + str(valor_2) + ' es ' + str(resultado))
    else:
        # Este error no debería suceder
        print('Respuesta no válida')
    
    return resultado

while True:
    valor_1 = numero_uno()
    valor_2 = numero_dos()
    
    respuesta = obten_resp()
    
    operacion(respuesta)
    
    
    
    seguir = input('¿Te gustaría seguir? (y/n): ').lower()
    if seguir == 'n':
        break
