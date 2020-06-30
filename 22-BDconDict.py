print('BD con Diccionario App\n')

admins = {
    'admin':'admin',
}

usuarios = {
    'gbullits':'r3v0luti0n',
    'dldamian':'nintendo',
    'balamdeus':'k4if4n3s',
}

intentos = 1
while intentos <= 5:
    usuario = input('Escribe tu usuario: ')
    if usuario in usuarios.keys() or usuario in admins.keys():
        break
    else:
        print('Usuario no reconocido, te quedan ' + str(5-intentos) + ' intentos')
        intentos += 1

intentos = 1
if usuario in admins.keys():
    while intentos <= 5:
        password = input('Ingresa tu contraseña: ')
        if password in admins[usuario]:
            print('¡Hola ' + usuario + '! Has iniciado sesión')
            print('\nEsta es la base de datos de los usuarios: ')
            for k,v in usuarios.items():
                print('\tUsuario: ' + k + '\t Contraseña: ' + v)
            break
        else:
            print('Contraseña incorrecta, te quedan ' + str(5-intentos) + ' intentos')
            intentos += 1
elif usuario in usuarios.keys():
    while intentos <= 5:
        password = input('Ingresa tu contraseña: ')
        if password in usuarios[usuario]:
            print('¡Hola ' + usuario + '! Has iniciado sesión')
            while True:
                cambiar_pass = input('¿Deseas cambiar tu contraseña? (y/n): ').lower()
                if cambiar_pass == 'y':
                    while True:
                        nuevas_pass = input('Escribe tu nueva contraseña: ')
                        if len(nuevas_pass) > 7:
                            usuarios[usuario] = nuevas_pass
                            print('\nTu nueva contraseña ha sido actualizada')
                            break
                        else:
                            print('Tu nueva contraseña debe tener al menos 8 caracteres')
                    break
                elif cambiar_pass == 'n':
                    print('Okey. Adios')
                    break
                else:
                    print('Respuesta no válida')
            break
        else:
            print('Contraseña incorrecta, te quedan ' + str(5-intentos) + ' intentos')
            intentos += 1
    
        
else:
    print('No pudiste iniciar sesión.')
    
if intentos == 6:
        print('No pudiste iniciar sesión')
        