t = 'DESAFIO 55 - CLASSIFICADOR DE PESOS - FOR'
print('{:=^105}'.format(t))

maior = 0
menor = 0
for c in range(1,6):
    p = float(input('Digite o peso em kg da {}° pessoa  '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

print('O maior peso é {} kg'.format(maior))
print('O menor peso é {} kg'.format(menor))