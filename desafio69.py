t = 'CADRASTRO DE PESSOAS (BREAK)'
print(f'{t:=^105}')

from datetime import date
atual = date.today().year
#print(atual)

i = 's'
s = 's'
continuar = ' '
m = 0
f = 0
p = 0
while True:
    print('-' * 25)
    print(' CADASTRE UMA PESSOA')
    print('-' * 25)
    i = int(input('Idade: '))
    s = continuar = ' '
    while s not in 'MmFf':
        s = str(input('Sexo[M/F]: ')).upper().strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Quer Continuar [S/N]?')).upper().strip()
    if s == 'M':
        m += 1
    if s == 'F' and i <= 20:
        f += 1
    if i >= 18:
        p += 1
    if continuar == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {p}
Ao todo temos {m} homens cadastrados cadastrados
E temos {f} mulheres com menos de 20 anos''')