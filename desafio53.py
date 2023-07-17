t = 'DESAFIO 53 - VERIFICADOR DE PALINDROMOS - FOR'
print('{:=^105}'.format(t))


f = str(input('Digite sua frase: \n')).strip().upper()
p = f.split()
j = ''.join(p)
#print(f)
#print(j)
#ji = j[::-1]
#print('De tra para frente sua frase fica: {}'.format((ji)))
#print('Por sua vez a frase original é {}'.format(j))


#solução única Python►
#if str(j) == str(j)[::-1]: #str de traz para frente
#    print('É um palindromo')
#else:
#    print('Não é um palindromo!')

#solução com for

inverso = ''

for c in range(len(j)-1,-1,-1):
    inverso +=j[c]
if inverso == j:
    print('Palindromo!')
else:
    print('Nope!')
print(j)
print(inverso)