t = str('DESAFIO 41 - CATEGORIAS DE NATAÇÃO (ELIF)')
print('{:=^105}'.format(t))

from datetime import date

#inputs
ano = int(input('Qual seu ano de nascimento?'))
atual = date.today().year
i = int(atual - ano)
#i = int(input('Qual sua idade? '))

#saídas
if 25 < i:
    print('Sua idade é {} e o senhor(a) fica na categoria MASTER'.format(i))
elif i <= 9:
    print('Sua idade é {} e o senhor (a) fica na categoria MIRIM'.format(i))
elif 14 >= i > 9:
    print('Sua idade é {} e o senhor (a) fica na categoria INFANTIL'.format(i))
elif 19 >= i > 14:
    print('Sua idade é {} e o senhor (a) fica na categoria JUNIOR'.format(i))
elif 25 >= i > 19:
    print('Sua idade é {} e o senhor (a) fica na categoria SENIOR'.format(i))