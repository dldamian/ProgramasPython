print('Tipos de listas y sus datos')

num_strings = ['15','100','55','42']
num_ints = [15,100,55,42]
num_floats = [2.2,5.0,1.245,0.134]
num_lists = [[1,2,3],[4,5,6],[7,8,9]]

print('\nLa variable num_strings es del tipo ' + str(type(num_strings)))
print('Contiene los elementos: ' + str(num_strings))
print('El elemento ' + num_strings[0] + ' es del tipo ' + str(type(num_strings[0])))

print('\nLa variable num_ints es del tipo ' + str(type(num_ints)))
print('Contiene los elementos: ' + str(num_ints))
print('El elemento ' + str(num_ints[0]) + ' es del tipo ' + str(type(num_ints[0])))

print('\nLa variable num_floats es del tipo ' + str(type(num_floats)))
print('Contiene los elementos: ' + str(num_floats))
print('El elemento ' + str(num_floats[0]) + ' es del tipo ' + str(type(num_floats[0])))

print('\nLa variable num_lists es del tipo ' + str(type(num_lists)))
print('Contiene los elementos: ' + str(num_lists))
print('El elemento ' + str(num_lists[0]) + ' es del tipo ' + str(type(num_lists[0])))

print('\nAhora vamos a ordenar las listas num_strings y num_ints')
num_strings.sort()
print(num_strings)
num_ints.sort()
print(num_ints)
print('\nLas listas tipo string se ordenan por orden alfabético, mientas que las listas tipo int se ordenan numericamente')
