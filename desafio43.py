t = str('DESAFIO 43 - IMC (ELIF)')
print('{:=^105}'.format(t))

#inputs
p = float(input('Qual seu peso em kg? '))
a = float (input('Qual sua altura em m? '))
imc = p / a**2

#outputs:
if imc < 18.5:
    print('Seu IMC é {:.2f}, ficando na categoria ABAIXO DO PESO'.format(imc))
elif 25 > imc >= 18.5:
    print('Seu IMC é {:.2f}, ficando na categoria PESO IDEAL'.format(imc))
elif 30 > imc >= 25:
    print('Seu IMC é {:.2f}, ficando na categoria SOBREPESO'.format(imc))
elif 40 > imc >= 30:
    print('Seu IMC é {:.2f}, ficando na categoria OBESIDADE'.format(imc))
else:
    print('Seu IMC é {:.2f}, ficando na categoria OBESIDADE MÓRBIDA'.format(imc))