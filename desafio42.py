t = str('DESAFIO 42 - CLASSIFICAÇÃO DOS TRIANGULOS')
print('{:=^105}'.format(t))

#inputs:
r1 = float(input('Tamanho da reta 1:'))
r2 = float(input('Tamanho da reta 1:'))
r3 = float(input('Tamanho da reta 1:'))

#saídas:
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1+r2):
    print('É um triângulo!')
    if r1 == r2 ==r3:
        print('Tipo equilátero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Tipo Isósceles')
    else:
        print('Tipo Escaleno')
else:
    print('Não é um trinagulo')
