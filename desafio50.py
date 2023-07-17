t = 'DESAFIO 50 - SOMA DE NÚMEROS PARES- VERSÃO FOR'
print('{:=^105}'.format(t))


soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor inteiro: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você digitou {} numeros pares e a some é {}'.format(cont, soma))