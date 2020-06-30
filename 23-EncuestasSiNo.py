print('Encuestas SI o NO APP')

pregunta = input('\n¿Cuál es la encuesta a resolver?: ').title()
while True:
    participantes = input('¿Cuántos participantes tendrá la encuesta?: ')
    try:
        participantes = int(participantes)
        if participantes >= 1:
            break
        else:
            print('Debe haber al menos 1 participante')
    except:
        print('Solo números enteros')

password = input('Escribe la contraseña para consultar los resultados: ')

respuestas = {}
participante = 1
si = 0
no = 0
while participante <= participantes:
    nombre = input('\nEscribe tu nombre: ').title()
    if nombre not in respuestas:
        print('Aquí está la pregunta: ¿' + pregunta)
        respuesta = input('Escribe tu respuesta: (SI/NO): ').upper()
        if respuesta == 'SI':
            respuestas[nombre] = respuesta
            si += 1
            print('Gracias por tu respuesta ' + nombre)
        elif respuesta == 'NO':
            respuestas[nombre] = respuesta
            no += 1
            print('Gracias por tu respuesta ' + nombre)
        else:
            print('Gracias por tu respuesta ' + nombre)
            print('No es una respuesta que esperabamos...pero ok')
            respuestas[nombre] = respuesta
        participante += 1
    else:
        print('Tu ya votaste')

print('\nLas siguientes personas votaron:')
for k in respuestas.keys():
    print(k)
        
print('\nDe la siguiente pregunta: ¿' + pregunta )
if si > no:
    print('La respuesta SÍ ganó con ' + str(si) + ' voto, sobre ' + str(no) + ' voto(s) sobre NO')
elif no > si:
    print('La respuesta NO ganó con ' + str(no) + ' voto, sobre ' + str(si) + ' voto(s) sobre SÍ')
else:
    print('Hubo un empate: ' + str(si) + ' voto(s) sobre SÍ y ' + str(no) + ' voto(s) sobre NO')
    
ver_resultados = input('\n¿Quieres saber todos los resultados? Escribe la contraseña: ')
if ver_resultados == password:
    for k, v in respuestas.items():
        print('Votante: ' + k + '\tVoto: ' + v)
else:
    print('Contraseña incorrecta. Adios')