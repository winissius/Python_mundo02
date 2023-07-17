t = 'DESAFIO 58, CONDIÇÕES: JOGO DA ADIVINHAÇÃO 2.0'
print('{:=^105}'.format(t))

import random

n = random.randint(1, 10)
print(n)
from time import sleep # função que faz o pc esperar x segundos para responder!

guess = int(input('Entre 1 e 10, escolha um número:\n'))

print('PROCESSANDO')
sleep(2)
count = 1
while guess !=n:
    count += +1
    if guess < n:
        print('Maior...')
        guess = int(input('Tente outra vez...'))
    elif guess > n:
        print('Menor...')
        guess = int(input('Tente outra vez...'))
print('Você acertou em {} tentativas, eu escolhi {}'.format(count,n))


