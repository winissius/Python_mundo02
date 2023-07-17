t = 'DESAFIO 61 - PROGRESSÃO ARITMÉTICA - (WHILE)'
print('{:=^105}'.format(t))

n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
t = 10
c1 = 0
c2 = 0

while c1 != 11:
    if c1 <10:
        print(n, end = ' -> ')
        n = n+r
        c1 += 1
    elif c1 == 10:
        t2 = int(input('Mais quantos números na PA? '))
        if t2 == 0:
            c1 = 11
        else:
            c1 = c1 - t2
print('FIM')
