t = str('DESAFIO 40 - MÉDIA DE ALUNOS (ELIF)')
print('{:=^105}'.format(t))

n1 = float(input('Nota do primeiro bimestre: '))
n2 = float(input('Nota do segundo bimestre: '))
m=(n1+n2)/2

if m >= 7:
    print('Aprovado!')
elif 6.9 >= m >= 5:
    print('Recuperação!')
else:
    print('Reprovado!')