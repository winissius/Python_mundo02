t = str(' DESAFIO 45 - PEDRA, PAPEL OU TESOURA ')
print('{:=^105}'.format(t))

from random import choice
from time import sleep
from random import randint
# imput

j = str(input('Vamos jogar Jokenpo, pedra é P, tesoura é T e papel é L. Vamos lá! ').lower())
p = str('p')
t = str('t')
l = str('l')
jb = [p, t, l]
sleep(1)
jc = choice(jb)
"""""#outra forma
itens = ('p','l','t')
jc_randint = randint(0, 2)
jc = itens[jc_randint]"""
print ('{}'.format(jc))

if j == jc:
    print('Empate, de novo!')
elif j == p and jc == t:
    print('Você jogou Pedra, eu Tesoura, você ganhou!')
elif j == p and jc == l:
    print('Você jogou Pedra, eu Papel, eu ganhei!')
elif j == t and jc == p:
    print ('Você jogou Tesoura, eu Pedra, eu ganhei!')
elif j == t and jc == l:
    print ('Você jogou Tesoura, eu Papel, você ganhou!')
elif j == l and jc == p:
    print ('Você jogou Papel, eu Pedra, você ganhou!')
elif j == l and jc == t:
    print ('Você jogou Papel, eu Tesoura, eu ganhei!')

