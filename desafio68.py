t = 'DESAFIO 48 - PAR OU IMPAR (BREAK)'
print(f'{t:=^105}')

print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)

from random import randint

c = 0

while True:
    vc = randint(1, 10)
    #print(vc)
    v = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PpIi':
        pi = str(input('Par ou Ímpar [P/I]')).strip().upper()[0]
    t = vc +v
    if t % 2 == 0:
        r = 'P'
        d = 'PAR'
    if t % 2 != 0:
        r = 'I'
        d = 'ÍMPAR'
    print('-' * 15)
    print(f'Você jogou {v} e o computador {vc}. Total foi {t} DEU {d}!')
    print('-' * 15)
    if pi != r:
        break
    c += 1
    print('Você VENCEU!')
    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {c} vezes')



