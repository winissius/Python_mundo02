t = str('DESAFIO 38 - COMPARAÇÃO DE DOIS NUMEROS (ELIF)')

print('{:=^105}'.format(t))

a = int(input('Primeiro número inteiro: '))
b = int(input('Segundo numero inteiro: '))

if a > b:
    print('O primeiro valor digitado é maior ')
elif b > a:
    print('O segundo valor digitado é maior')
else:
    print('Os números são iguais')