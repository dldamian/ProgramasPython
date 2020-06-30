
abecedario = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'ñ':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,
    }

frase = input('Ingresa una frase: ').lower()
for c in frase:
    if c == 'a':
        abecedario[c] +=1
    elif c == 'b':
        abecedario[c] +=1
    elif c == 'c':
        abecedario[c] +=1
    elif c == 'd':
        abecedario[c] +=1
    elif c == 'e':
        abecedario[c] +=1
    elif c == 'f':
        abecedario[c] +=1
    elif c == 'g':
        abecedario[c] +=1
    elif c == 'h':
        abecedario[c] +=1
    elif c == 'i':
        abecedario[c] +=1
    elif c == 'j':
        abecedario[c] +=1
    elif c == 'k':
        abecedario[c] +=1
    elif c == 'l':
        abecedario[c] +=1
    elif c == 'm':
        abecedario[c] +=1
    elif c == 'ñ':
        abecedario[c] +=1
    elif c == 'o':
        abecedario[c] +=1
    elif c == 'p':
        abecedario[c] +=1
    elif c == 'q':
        abecedario[c] +=1
    elif c == 'r':
        abecedario[c] +=1
    elif c == 's':
        abecedario[c] +=1
    elif c == 't':
        abecedario[c] +=1
    elif c == 'u':
        abecedario[c] +=1
    elif c == 'v':
        abecedario[c] +=1
    elif c == 'w':
        abecedario[c] +=1
    elif c == 'x':
        abecedario[c] +=1
    elif c == 'y':
        abecedario[c] +=1
    elif c == 'z':
        abecedario[c] +=1
    else:
        pass

print('\nResultados')
print('Letra \t\t Ocurrencia \tPorcentaje')
total_letras = 0
for k,v in abecedario.items():
    if v >= 1:
        total_letras += 1
        
for k,v in abecedario.items():
    if v >= 1:
        print(k + '\t\t' + str(v) + '\t\t' + str(round((v*100)/total_letras,2)) + '%')
        