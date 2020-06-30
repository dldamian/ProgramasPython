import random

print('Tesauro APP\n')

tesauros = {
    'caliente':['tropical','verano','sol'],
    'frio':['invierno','helado','polar'],
    'feliz':['contendo','alegre','sonriente'],
    'triste':['infeliz','melancólico','miserable']
}

print('Escoge una palabra de la lista de Tesauros disponibles:')

for k in tesauros.keys():
    print('\t' + k)

while True:
    palabra = input('\nEscribe la palabra de la que quieras saber un sinónimo: ').lower()
    if palabra in tesauros.keys():
        break
    else:
        print('Esa palabra no está en la lista')

print('Un sinónimo de ' + palabra + ' es: ' + tesauros[palabra][random.randint(0,2)])

while True:
    saber = input('¿Te gustaría saber todos los Tesauros disponibles? (y/n): ').lower()
    if saber == 'y':
        for k in tesauros.keys():
            print('Los sinónimos de ' + k + 'son:')
            for v in tesauros.values:
                print(v)
        break
    elif saber == 'n':
        print('Okey, adios...')
        break
    else:
        print('Respuesta no válida')
