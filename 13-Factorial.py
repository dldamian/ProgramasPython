import math

resultado = 1

while True:
    num = input('Escribe el número que deseas saber su factorial: ')
    try:
        num = int(num)
        if num <= 0:
            print('Números mayor a 0')
        else:
            break
    except:
        print('Solo números enteros')
        
print(str(num) + '! = ', end='')

for i in range(1,num):
    print(str(i),end='*')
print(str(num))
    
for n in range(1,num+1):
    resultado = resultado * n

print('\n\nEl resultado con el método "for" es: ' + str(resultado))
print('El resultado con el método módulo math es: ' + str(math.factorial(num)))

print('\n¡Se demostró 2 veces que el resultado de ' + str(num) + '! es ' + str(resultado) + '!')