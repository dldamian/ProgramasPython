def mostrarEstado(nombre):
    print('\nResumen de la cuenta de ' + nombre)
    print('Cuenta Personal: $' + str(usuarios[nombre]['Cuenta Personal']))
    print('Cuenta Ahorros: $' + str(usuarios[nombre]['Cuenta Ahorros']))
        
        
def nuevoUsuario(nombre):
    usuarios[nombre] = {
    'Cuenta Personal':0,
    'Cuenta ahorros':0
    }
    
def agregarSaldoPersonal():
    while True:
        cantidad = input('Ingresa la cantidad que deseas depositar: ')
        try:
            cantidad = float(cantidad)
            if cantidad >= 0:
                usuarios[nombre]['Cuenta Personal'] += cantidad
                print('Se han añadido $' + str(cantidad) + ' a tu Cuenta Personal')
                break
            else:
                print('No se puede agregar a tu cuenta un número negativo')
                cancelar = input('¿Deseas cancelar la operación? (y/n): ').lower()
                if cancelar == 'y':
                    break
        except:
            print('Ingresa solo números')
            cancelar = input('¿Deseas cancelar la operación? (y/n): ').lower()
            if cancelar == 'y':
                break
    
def agregarSaldoAhorros():
    while True:
        cantidad = input('Ingresa la cantidad que deseas depositar: ')
        try:
            cantidad = float(cantidad)
            if cantidad >= 0:
                usuarios[nombre]['Cuenta Ahorros'] += cantidad
                print('Se han añadido $' + str(cantidad) + ' a tu Cuenta Ahorros')
                break
            else:
                print('No se puede agregar a tu cuenta un número negativo')
                cancelar = input('¿Deseas cancelar la operación? (y/n): ').lower()
                if cancelar == 'y':
                    break
        except:
            print('Ingresa solo números')
            cancelar = input('¿Deseas cancelar la operación? (y/n): ').lower()
            if cancelar == 'y':
                break

                
def retiroSaldoPersonal():
    while True:
        cantidad = input('Ingresa la cantidad que deseas retirar: ')
        try:
            cantidad = float(cantidad)
            if cantidad <= usuarios[nombre]['Cuenta Personal']:
                usuarios[nombre]['Cuenta Personal'] -= cantidad
                print('Se ha retirado $' + str(cantidad) + ' de tu Cuenta Personal')
                break
            else:
                print('No se puede retirar esa cantidad. Tu cuenta quedaría en negativo')
                cancelar = input('¿Desead cancelar la operación? (y/n): ').lower()
                if cancelar == 'y':
                    break
        except:
            print('Ingresa solo números')
            cancelar = input('¿Deseas cancelar la operación? (y/n): ').lower()
            if cancelar == 'y':
                break
                
def retiroSaldoAhorros():
    while True:
        cantidad = input('Ingresa la cantidad que deseas retirar: ')
        try:
            cantidad = float(cantidad)
            if cantidad <= usuarios[nombre]['Cuenta Ahorros']:
                usuarios[nombre]['Cuenta Ahorros'] -= cantidad
                print('Se ha retirado $' + str(cantidad) + ' de tu Cuenta Ahorros')
                break
            else:
                print('No se puede retirar esa cantidad. Tu cuenta quedaría en negativo')
                cancelar = input('¿Deseas cancelar la operación? (y/n): ').lower()
                if cancelar == 'y':
                    break
        except:
            print('Ingresa solo números')
            cancelar = input('¿Deseas cancelar la operación? (y/n): ').lower()
            if cancelar == 'y':
                break
                

def queCuenta():
    while True:
        cuenta = input('¿Qué cuenta te gustaría consultar? (Personal/Ahorros): ').title()
        if cuenta == 'Personal':
            break
        elif cuenta =='Ahorros':
            break
        else:
            print('Opción no válida')
    return cuenta

def queOperacion():
    while True:
        operacion = input('¿Qué acción? te gustaría consultar? (Deposito/Retiro): ').title()
        if operacion == 'Deposito':
            break
        elif operacion =='Retiro':
            break
        else:
            print('Opción no válida')
    return operacion
                
usuarios = {
    'Leonardo Damian':{
        'Cuenta Personal':0,
        'Cuenta Ahorros':0,
    },
    'Pavel Octavio':{
        'Cuenta Personal':0,
        'Cuenta Ahorros':0,
    }
} 

print('Bienvenido al Simulador de Banco')

while True:
    nombre = input('Ingresa tu nombre: ').title()
    if nombre in usuarios.keys():
        break
    else: 
        print('No estás inscrita en este banco, ¿Deseas abrir una cuenta?')
        agregar = input('¿Deseas inscribirte al banco? (y/n): ')
        if agregar == 'y':
            nuevoUsuario(nombre)
            break
            
        
while True:        
    mostrarEstado(nombre)
    
    cuenta = queCuenta()
    print(cuenta)
    operacion = queOperacion()
    print(operacion)
    if cuenta == 'Personal':
        if operacion == 'Deposito' or operacion == 'Depósito':
            agregarSaldoPersonal()
        else:
            retiroSaldoPersonal()
    else:
        if operacion == 'Deposito' or operacion == 'Depósito':
            agregarSaldoAhorros()
        else:
            retiroSaldoAhorros()
    
    print('\nTu nuevo estado de cuenta es así:')
    mostrarEstado(nombre)
    
    
    reinicio = input('¿Deseas hacer otra transacción?: (y/n): ')
    if reinicio == 'n':
        break
        
print('Gracias por usar la app')