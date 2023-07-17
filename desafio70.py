t = 'DESAFIO 70 - LISTA DE PRODUTOS COMPRADOS (BREAK WHILE)'
print(f'{t:=^105}')
print('-'*25)
print('   LOJA SUPER BARATÃO')
print('-'*25)

t = c1000 = 0
count = 0
while True:
    n = str(input('Nome do produto: '))
    v = float(input('Preço: R$ '))
    c = ' '
    t += v
    count +=1
    if count ==1 or v < menor:
        menor = v
        nmenor = n
    '''if count == 1: # outra forma de resolver a forma a cima é mais simples
        menor = v
        nmenor = n
    if v < menor:
        menor = v
        nmenor = n'''
    while c not in 'NS':
        c = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if v > 1000:
        c1000 += 1
    if c == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {t}')
print(f'Temos {c1000} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {nmenor} que custa R${menor:.2f}')