t = 'DESAFIO 59 - MENU PARA OPERAÇÃO COM 2 NÚMEROS (WHILE)'
print('{:=^105}'.format(t))

print('..........INICIANDO..........')

#inputs:
n1 = float(input('Digite um número '))
n2 = float(input('Digite outro número '))
o = 0

#outputs
while o != 5:
    print('''Digite a operação que desejar fazer com os números'
              [1] SOMA
              [2] MULTIPLICAÇÃO
              [3] MAIOR
              [4] NOVOS NÚMEROS
              [5] SAIR DO PROGRAMA''')
    o = int(input(''))
    if o == 1:
        print('A soma de {} e {} é {}'.format(n1,n2,n1+n2))
    elif o == 2:
        print('A multiplicação de {} e {} é {}'.format(n1,n2,n1 * n2))
    elif o == 3:
        if n1 < n2:
            maior = n2
        else:
            maior = n1
        print('O maior entre {} e {} é {}'.format(n1,n2,maior))
    elif o == 4:
        n1 = float(input('Digite um novo número '))
        n2 = float(input('Digite outro novo número '))
    elif o !=5:
        print('Opção inválida')

print('\n..........FINALIZANDO..........')
print('\nObrigado por utilizar nosso programa')
