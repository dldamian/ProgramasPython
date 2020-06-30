print('Convertidor al convertidor de Temperaturas')

while True:
    fahrenheit = input('Ingresa los grados Fahrenheit que deseas convertir: ')
    try:
        fahrenheit = float(fahrenheit)
        conversionCelcius = round(((fahrenheit - 32)*(5/9)),4)
        conversionKelvin = round(((fahrenheit - 32)*(5/9) + 273.15),4)
        print(f'Fahrenheit: \t\t{fahrenheit}')
        print(f'Fahrenheit a Celcius: \t{conversionCelcius}')
        print(f'Fahrenheit a Kelvin: \t{conversionKelvin}')
        break
    except:
        print('Ingresa un número.')