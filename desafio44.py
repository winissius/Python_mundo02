t = ' DESAFIO 44 - PREÇO E FORMA DE PAGAMENTO '
print('{:=^105}'.format(t))

p = float(input('Informe o preço do produto: '))
f = int(input('Digite a forma de pagamento:\n' \
             '1 - a vista no dinheiro\n' \
             '2 - a vista no cartão\n' \
             '3 - em até duas vezes no cartão\n' \
             '4 - em três ou mais vezes no cartão\n'))

if f == 1:
    v = p * .9
elif f == 2:
    v = p * 0.95
elif f == 3:
    v = p
else:
    v = p * 1.2
print('O preço do produto é R$ {:.2f}, mas nessa forma de pagamento podemos fazer R$ {:.2f}'.format(p,v))