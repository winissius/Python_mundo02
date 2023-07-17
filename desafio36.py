t = str('DESAFIO 36 - EMPRESTIMO BANCARIO')

print('{:=^105}'.format(t))

#variáveis
casa = float(input('Qual o valor do imóvel?'))
sal = float(input('Qual sua renda mensal?'))
anos = int(input('Quantos anos deseja para pagar?'))
p = casa/(anos*12)

#resultados


if p >= 0.3*sal:
    print('Infelizmente o seu emprestimo não foi aprovado.')

else:
    print('O valor da sua prestação mensal será R${:.2f}'.format(p))