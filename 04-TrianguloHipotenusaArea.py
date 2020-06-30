import math

print('Calculador de Hipotenusa y Área de un Triángulo')
iniciador = True

while iniciador:
    lado1 = input('Ingresa el primer lado del triángulo: ')
    try:
        lado1 = float(lado1)
        while isinstance(lado1, float) is True:
            lado2 = input('Ingresa el segundo lado del triángulo: ')
            try:
                lado2 = float(lado2)
                hipotenusa = round(math.sqrt(lado1**2 + lado2**2),3)
                area = round((lado1*lado2)/2,3)
                print('='*10)
                print(f'La Hipotenusa de un triángulo cuyos lados sean {lado1} y {lado2} es: \t{hipotenusa}')
                print(f'El Área de un triángulo cuyos lados sean {lado1} y {lado2} es: \t{area}')
                iniciador = False
                break
            except:
                print('Ingresa solo números')
                continue
    except:
        print('Ingresa solo números')