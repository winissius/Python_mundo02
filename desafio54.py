t = 'DESAFIO 54 - CONTADOR DE ANIVERSÁRIOS - FOR'
print('{:=^105}'.format(t))

from datetime import date
atual = date.today().year
#print(atual)

cm = 0 #maiores
cn = 0 #menores
for p in range(0,2):
    i = int(input('Ano de nasicmento: '))
    if (atual - i) >= 18:
        cm += 1
    else:
        cn +=1
print('De todos vocês {} já são maiores e {} ainda não'.format(cm, cn))