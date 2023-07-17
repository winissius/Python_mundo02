t = 'DESAFIO 64 - TRATANDO VÁRIOS NUMEROS - WHILE'
print('{:=^105}'.format(t))

n = 1
c = 0
s = 0
n = int(input('Digite um valor ')) # gambiara a ser resolvida na aula 15
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um valor '))# gambiara a ser resolvida na aula 15
print('você digitou {} valores'.format(c))
print('Sua soma foi {}'.format(s))


