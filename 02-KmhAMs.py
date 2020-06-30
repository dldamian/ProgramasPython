print('Convertidor de KM/H (Kilometros por hora) a M/S (Metros por segundo')

while True:
    km = input('Ingresa la cantidad en KM/H que deseas convertir a M/S: ')
    try:
        km = float(km)
        conversion = round(km*(5/18),2)
        print(f'Tu velocidad en metros por segundo es: {conversion}')
        break
    except:
        print('Ingresa un número.')