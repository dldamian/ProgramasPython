import cmath

print('''Resolución de Ecuaciones de Segundo Grado\n
Una ecuación de segundo grado tiene la siguiente fórmula: ax^2 + bx + c = 0.
Las soluciones pueden ser reales o números complejos.
Un número complejo tiene dos partes: a + bj
Donde a es una porción real y bj es una porción imaginaria.
''')

while True:
    contador = input('¿Cuántas ecuaciones quieres resolver hoy?: ')
    try:
        contador = int(contador)
        break
    except:
        print('Introduce solo números enteros')

for i in range(contador):
    print('\nResolviendo la ecuación #' + str(i+1))
    print('*'*30)
    while True:
        a = input('Introduzca el valor de "a" (coeficiente de x^2) = ')
        try:
            a = float(a)
            break
        except:
            print('Introduce solo números')

    while True:
        b = input('Introduzca el valor de "b" (coeficiente de x) = ')
        try:
            b = float(b)
            break
        except:
            print('Introduce solo números')

    while True:
        c = input('Introduzca el valor de "c" (coeficiente) = ')
        try:
            c = float(c)
            break
        except:
            print('Introduce solo números')

    print('\nLas soluciones para ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0 son:')
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
    print('\tx1 = ' + str(x1))
    print('\tx2 = ' + str(x2))

print('\nGracias por usar el programa')