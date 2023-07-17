t = 'DESAFIO 49 - TABUADA 2.0 - VERSÃO FOR'
print('{:=^105}'.format(t))

n = int(input('Escolha seu número: '))

for c in range(1, 11):
    t = n * c
    print('{} x {:2} = {}'.format(n, c, t))