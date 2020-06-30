print('Bienvenido al contador de letras\n')

nombre = input('Por favor escribe tu nombre: ').title()
print('Hola ' + nombre + ', contaré todas las veces que una letra se repite de un mensaje específico. \n')

mensaje = input('Por favor ingresa un mensaje: ').lower()
letra = input('Por favor ingresa la letra que desees que cuente: ').lower()

contador = mensaje.count(letra)

print(f'La letra "{letra}" aparece {contador} veces en el mensaje')