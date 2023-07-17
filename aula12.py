t = str('Aula 12 - CONDIÇÕES ANINHADAS')
print('{:=^105}'.format(t))

nome = str(input('Qual seu nome?'))
if nome == 'Dedessa':
    print('Que nome lindo!')
elif nome == 'Winissius' or nome == 'Mingoso' or nome == 'Mima Valentina':
    print('Nome diferente!')
elif nome in ('Andressa Deds Dedinha'):
    print('Nome delicia')
else:
    print('Nome normal')
print('Tenha um bom dia, {}!'.format(nome))