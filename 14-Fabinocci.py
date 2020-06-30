print('Fibonacci APP')

while True:
    n = input('\n¿Cuántos dígitos de la secuencia Fibonacci te gustaría mostrar?: ')
    try:
        n=int(n)
        break
    except:
        print('Solo números enteros')
        
fib = [1,1]

for i in range(n-2):
    nuevo_fib = fib[i] + fib[i+1]
    fib.append(nuevo_fib)
    
print('\nLos primeros ' + str(n) + ' números de la secuencia Fibonacci son:')
for i in fib:
    print(i)
    

golden = []    
for i in range(len(fib)-1):
    radio = fib[i+1] / fib[i]
    golden.append(radio)
    
print('\nSus correspondientes proporción áurea son:')
    
for g in golden:
    print(str(g))


print('\nLa relación de términos consecutivos de Gibonacci se aproxima a Phi: 1.618 ...')