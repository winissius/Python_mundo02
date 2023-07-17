t = 'DESAFIO 52 - NÚMEROS PRIMOS - FOR'
print('{:=^105}'.format(t))

n = int(input('Digite o número que deseja verificar se é primo: '))

count = 0
soma = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\33[34m', end = ' ')
    else:
        print('\33[31m', end = ' ')
    print('{}'.format(c), end=' ')
    if n % c == 0:
        soma +=1
#print(soma)
print('\n\n\33[m''O número {} foi divisivel {} vezes'.format(n, soma))
if soma == 2:
    print('Então ele é Primo')
else:
    print('Então ele Nâo é primo')
