t = 'DESAFIO 65 - MAIOR E MENOR DE VÁRIOS VALORES - WHILE'
print('{:=^105}'.format(t))

s = count = 0
c = 'S'
menor = maior = 0
while c != 'N':
    n = int(input('Digite um número '))
    s +=n
    count +=1
    if count == 1: # sempre declarar maior e menor no inicio
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    m = s/count
    c = str(input('Quer continuar [[S/N] ')).upper().strip()[0]
    '''if c != 'S':
        print('Opção inválida')'''
print('você digitou {} números'.format(count))
print('a média dos números é {}'.format(m))
print('o menor número digitado foi {} e o maior foi {}'.format(menor, maior))
