t = 'DESAFIO 62 - FIBONACCI (WHILE)'
print('{:=^105}'.format(t))
#inputs
n = int(input('Quantos numeros de Fibo você quer? '))
f1 = 0
f2 = 1
c = 3
#outputs
print('{} - {}'.format(f1, f2), end = '')
while c <= n:
    f3 = f1 + f2
    print(' - {} '.format(f3), end='')
    f1 = f2
    f2 = f3
    c += 1
print(' - Fim!')
