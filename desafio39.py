t = str('DESAFIO 39 - ALISTAMENTO MILIAR (ELIF)')

print('{:=^105}'.format(t))

import datetime

#now = datetime.datetime.now() # outra forma
#atual = '{:02d}'.format(now.year) #outra forma
atual = datetime.date.today().year

print(atual)

i = int(input('Qual seu ano de nascimento? '))

if int(atual) - i < (18):
    print('Você precisará se alsitar em {} anos'.format((18)-(int(atual)-i)))
elif int(atual) - i == 18:
    print('Você deve se alistar esse ano')
else:
    print('Você já deve ter se alistado a {} anos'.format(((int(atual)-i)-18)))



