t = 'DESAFIO 62 - super PROGRESSÃO ARITMÉTICA - (WHILE)'
print('{:=^105}'.format(t))

n = int(input('diga o primeiro termo:'))
r = int(input('diga a razão'))

c = 0
t = 10
k = 1

while k != 0:
    while c != t:
       p = n + r*c
       c += 1
       print(p)
    j = int(input('Quantos termos a mais ?'))
    t = c + j
    if j == 0:
        k = 0
print ('\n{} termos'.format(c))

print('FIM')
