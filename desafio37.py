t = str('DESAFIO 37 - CONVERSÃO DE NÚMERO INTEIRO')

print('{:=^105}'.format(t))

#1 binario
#2 octal
#3 hexadecimal

n = int(input('Digite um número inteiro: '))
c = str(input('Digite 1 para conversão binária, 2 para conversão octal e 3 para hexadecimal: '))

if c == '1':
    print('Você escolheu a conversão binária')
    nb = bin(n)
    print('Seu numero em base binária é: {}'.format((nb[2:])))
elif c=='2':
    print('Você escolheu a conversão octal')
    no = oct(n)
    print('Seu número em base octal é: {}'.format(no[2:]))
else:
    print('Você escolheu a onversão hexadecimal:')
    nh = hex(n)
    print('Seu número em base hexadecimal é: {}'.format(nh[2:]))