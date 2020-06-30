import random

print('Bienvenido al adivinador de Palabras APP')

palabras = {
    'Deportes':['Futbol','Tennis','Basquetball','Americano','Box'],
    'Frutas':['Manzana','Piña','Uva','Pera','Platano'],
    'Colores':['Rojo','Azul','Amarillo','Morado','Negro','Blanco']
}

iniciador = True
while iniciador:
    
    # Saber la categoría y respuesta a mostrar
    # Recopila todas las categorías existentes
    categorias = []
    for categoria in palabras.keys():
        categorias.append(categoria)
    
    # Se genera index al azar para saber una respuesta al azar
    index_categorias = random.randint(0,len(categorias)-1)
    categoria = categorias[index_categorias]
    
    # Esta sería la respuesta generada
    resp = palabras[categoria][random.randint(0,len(palabras[categoria])-1)]
    
    
    # Respuesta codificada
    respcod = (len(resp)*'-')
    codificado = list(respcod)
    
    
    # Muestra mensaje de la palabra y categoría seleccionada al azar
    print('Adivina la palabra de ' + str(len(resp)) + ' palabras de la categoría ' + categoria)
    
    print(''.join(codificado))
    
    # Inicia Loop para que el usuario responda
    intentos = 1
    while True:
        respuesta = input('\nEscribe la respuesta que creas correcta: ').title().strip()
        if respuesta == resp:
            print('¡Adivinaste! Solo te tomó ' + str(intentos) + ' intentos\n')
            break
        else:
            intentos += 1
            print('Intenta otra vez, aquí tienes una pista:')
            while True:
                indexletra = random.randint(0,len(codificado)-1)
                if codificado[indexletra] == '-':
                    codificado[indexletra] = resp[indexletra]
                    break
            print(''.join(codificado))
            if '-' not in codificado:
                print('Perdiste...toda la palabra fue revelada')
                break
    
    
    
    reinicio = input('¿Quieres jugar otra vez? (y/n): ').lower()
    if reinicio == 'n':
        iniciador = False
    
print('Gracias por jugar')