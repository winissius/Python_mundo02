t = 'DESAFIO 46 - CONTAGEM REGRESSIVA ANO NOVO'
print('{:=^105}'.format(t))

from time import sleep

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('Kabum!')