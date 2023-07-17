t = 'DESAFIO 51 - PROGRESSÃO ARITIMÉTICA (PA) - FOR'
print('{:=^105}'.format(t))

#inputs
p = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razão da PA: '))

#outputs
for c in range(p, (p+10*r), r):
    print('{}'.format(c), end=' -> ')
print('ACABOU')