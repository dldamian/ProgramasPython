print('Bienvenido a la Shipping APP\n')

usuarios = ['dldamian','paveldeus','irvadn','nandamin']

while True:
    usuario = input('Escribe tu usuario: ').lower()
    if usuario in usuarios:
        print('\nBienvenido ' + usuario + '\n\nLos precios actuales de envio son:\n')
        print('De 0 a 100: \t\t$5.20 c/u')
        print('De 100 a 500: \t\t$5.00 c/u')
        print('De 500 a 1000: \t\t$4.90 c/u')
        print('Más de 1000: \t\t$4.80 c/u')
        break
    else:
        print('Tu usuario no existe')

while True:
    cantidad = input('\n¿Cuántas unidades te gustaría comprar?: ')
    try:
        cantidad = int(cantidad)
        break
    except:
        print('Ingresa solo números enteros')

if cantidad < 100:
    print('El envio por ' + str(cantidad) + ' unidades te costará $' + str(round(cantidad*5.2,2)) + ' con un costo de $5.20 c/u')
elif cantidad < 500:
    print('El envio por ' + str(cantidad) + ' unidades te costará $' + str(round(cantidad*5,2)) + ' con un costo de $5.00 c/u')
elif cantidad < 1000:
    print('El envio por ' + str(cantidad) + ' unidades te costará $' + str(round(cantidad*4.9,2)) + ' con un costo de $4.90 c/u')
else:
    print('El envio por ' + str(cantidad) + ' unidades te costará $' + str(round(cantidad*4.8,2)) + ' con un costo de $4.80 c/u')

while True:
    tomar_orden = input('\n¿Te gustaría hacer el pedido? (y/n): ').lower()
    if tomar_orden == 'y':
        print('Okey, enviaremos tu orden de ' + str(cantidad) + ' unidades')
        break
    elif tomar_orden == 'n':
        print('¡Será la próxima!')
        break
    else:
        print('Respuesta no válida')