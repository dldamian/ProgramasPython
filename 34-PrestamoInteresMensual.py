import pylab as pl

print('Prestamos APP')

def cantidadPrestamo():
    while True:
        cantidad = input('¿Cuánto quieres que se te preste?: ')
        try:
            cantidad = float(cantidad)
            return cantidad
        except:
            print('Ingresa solo números')

def cantidadPago():
    while True:
        cantidad = input('¿Cuánto quieres pagar al mes?: ')
        try:
            cantidad = float(cantidad)
            return cantidad
        except:
            print('Ingresa solo números')
            
def intereses():
    while True:
        interes = input('¿Cuánto será el interes: ')
        try:
            interes = float(interes)
            return interes
        except:
            print('Ingresa solo números')
            
def deuda(total,pago,interes,total_pagado):
    mes = 0
    
    while True:
        deuda = {
        'Deuda':total,
        'Interes':interes,
        'Pago mensual':pago,
        'Total pagado':total_pagado,
        }
    
        
        print('\nInformación de la deuda en el mes ' + str(mes))
        for k,v in deuda.items():
            print(k +': ' + str(v))
        
        mes += 1
        meses.append(mes)
        
        total = round((total + (total*interes)) - pago,2)
        deuda['Deuda'] = total
        if total > 0:
            x.append(total)
            
        total_pagado += pago
        if total > prestamo:
            print('\nNunca podrías pagar la deuda')
            print()
            for k,v in deuda.items():
                print(k +': ' + str(v))
            break
        elif total <= 0:
            print(total_pagado)
            print('\nInformación de la deuda en el mes ' + str(mes))
            deuda['Deuda'] = 0
            deuda['Pago mensual'] = pago - (total*-1)
            total_pagado = total_pagado - (total*-1) 
            deuda['Total pagado'] = total_pagado 
            for k,v in deuda.items():
                print(k +': ' + str(v))
            break
    print('\nHas pagado $' + str(round(total_pagado,2)) + ' en total')
    print('Eso es $' + str(round((total_pagado)-prestamo,2)) + ' más de tu deuda original')
    
            

x = []
meses = []        
prestamo = cantidadPrestamo()
x.append(prestamo)
interes = intereses()
interes = interes/100

pagar = cantidadPago()
deuda(prestamo,pagar,interes,0)

if len(x) == len(meses):
    pl.plot(meses,x)
    pl.xlabel('Meses')
    pl.ylabel('Deuda')
    pl.title('Resumen de la deuda en gráfica')
    pl.show()