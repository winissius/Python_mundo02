t = 'DESAFIO 57 - ENTRADAS EM M OU F (WHILE)'
print('{:=^105}'.format(t))

s = 'k'

while s != 'M' and s != 'F':
    s = str(input('Digite o seu sexo [M/F]')).strip().upper()[0] #apenas a primeira letra
    if s != 'M' and s != 'F':
        print('Dados Inválidos, por favor digite novamente')
print('Obrigado, sexo {} armazenado com sucesso!'.format(s))

'''s = str(input('Digite o seu sexo [M/F]')).strip().upper()[0]  # apenas a primeira letra
while s not in 'MmFf':
    s = str(input('Dados inválidos, por favor digite seu sexo [M/F]')).strip().upper()[0]  # apenas a primeira letra
print('\nObrigado, sexo {} armazenado com sucesso!'.format(s))'''