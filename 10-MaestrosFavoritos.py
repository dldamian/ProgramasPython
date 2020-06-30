import random

print('Maestros Favoritos APP\n')

maestros = []

agregar_maestro = input('¿Quién es tu primer maestro favorito?: ').title()
maestros.append(agregar_maestro)
agregar_maestro = input('¿Quién es tu segundo maestro favorito?: ').title()
maestros.append(agregar_maestro)
agregar_maestro = input('¿Quién es tu tercer maestro favorito?: ').title()
maestros.append(agregar_maestro)
agregar_maestro = input('¿Quién es tu cuarto maestro favorito?: ').title()
maestros.append(agregar_maestro)

print('\nTus maestros favoritos son: ' + str(maestros))
print('Tus maestros favoritos ordenados alfabeticamente son: ' + str(sorted(maestros)))
print('Tus maestros favoritos ordenados reverso alfabético son: ' + str(sorted(maestros,reverse=True)))

print('\nTus 2 primeros maestros favoritos son: ' + maestros[0] + ' y ' + maestros[1])
print('Tus siguientes 2 maestros favoritos son: ' + maestros[2] + ' y ' + maestros[3])
print('Tu último maestro favorito es: ' + maestros[-1])
print('Tienes un total de: ' + str(len(maestros)) + ' maestros favoritos')

agregar_maestro = input('\nOops, parece que ' + maestros[0] + ' ya no es tu PRIMER maestro favorito...¿Quién es ahora tu primer maestro favorito?: ').title()
maestros.insert(0,agregar_maestro)

print('\nTus maestros favoritos son: ' + str(maestros))
print('Tus maestros favoritos ordenados alfabeticamente son: ' + str(sorted(maestros)))
print('Tus maestros favoritos ordenados reverso alfabético son: ' + str(sorted(maestros,reverse=True)))

print('\nTus 2 primeros maestros favoritos son: ' + maestros[0] + ' y ' + maestros[1])
print('Tus siguientes 2 maestros favoritos son: ' + maestros[2] + ' y ' + maestros[3])
print('Tu último maestro favorito es: ' + maestros[-1])
print('Tienes un total de: ' + str(len(maestros)) + ' maestros favoritos')

while True:
    quitar_maestro = input('\nDe repente ya no te gusta un maestro...¿A quién deseas eliminar? ').title()
    if quitar_maestro in maestros:
        maestros.remove(quitar_maestro)
        break
    else:
        print('Ese maestro no está en la lista')

print('\nTus maestros favoritos son: ' + str(maestros))
print('Tus maestros favoritos ordenados alfabeticamente son: ' + str(sorted(maestros)))
print('Tus maestros favoritos ordenados reverso alfabético son: ' + str(sorted(maestros,reverse=True)))

print('\nTus 2 primeros maestros favoritos son: ' + maestros[0] + ' y ' + maestros[1])
print('Tus siguientes 2 maestro favoritos son: ' + maestros[2] + ' y ' + maestros[3])
print('Tu último maestros favorito es: ' + maestros[-1])
print('Tienes un total de: ' + str(len(maestros)) + ' maestros favoritos')