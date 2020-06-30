import requests
import json
import random


def pregunta_cuatro():
    while True:
        respuesta = input('\nEscribe el número de la respuesta correcta: ')
        try:
            respuesta = int(respuesta)
            if respuesta == 1 or respuesta == 2 or respuesta == 3 or respuesta == 4:
                break
            else:
                print('Opción no válida')
        except:
            print('Opción no válida')
            
    return respuesta
            
def pregunta_dos():
    while True:
        respuesta = input('\nEscribe el número de la respuesta correcta: ')
        try:
            respuesta = int(respuesta)
            if respuesta == 1 or respuesta == 2:
                break
            else:
                print('Opción no válida, escribe 1 o 2')
        except:
            print('Opción no válida')
            
    return respuesta 


while True:
    
    r = requests.get('https://opentdb.com/api.php?amount=1')
    datos = r.json()
    categoria = datos['results'][0]['category']
    pregunta = datos['results'][0]['question']
    respuesta_correcta = datos['results'][0]['correct_answer']
    respuestas = datos['results'][0]['incorrect_answers']
    respuestas.append(respuesta_correcta)
    random.shuffle(respuestas)
    
    if r.status_code == 200:
        while True:
            if len(respuestas) == 4:
                print('\n' + pregunta)
                num = 1
                for resp in respuestas:
                    print(str(num) + ') ' + resp)
                    num +=1
                respuesta = pregunta_cuatro()
                break
            else:
                print('\n' + pregunta)
                num = 1
                for resp in respuestas:
                    print(str(num) + ') ' + resp)
                    num +=1
                respuesta = pregunta_dos()
                break
    else:
        print('Hubo un error de conexión')
        
    if respuestas[respuesta-1] == respuesta_correcta:
        print('¡Adivinaste!')
    else:
        print('Fallaste, la respuesta correcta era ' + respuesta_correcta)
        
    
    jugar = input('¿Quieres volver a jugar? (y/n): ').lower()
    if jugar == 'n':
        break
        
    
    