t = 'DESAFIO 71 - SIMULADOR DE CAIXA ELETRÔNICO'
print(f'{t:=^105}')

print('='*35)
print('{:^35}'.format('BANCO CEV'))
print('='*35)
v = int(input('Que valor quer sacar?'))
while True:
    #if v % 50 == 0:
    n50 = v//50
    n20 = (v - n50*50)//20
    n10 = (v - (n50*50 + n20*20))//10
    n1 = (v - (n50*50 + n20*20 + n10*10))//1
    if (v-(n50*50 + n20*20+n10*10+n1*1)) == 0:
        break
if n50 > 0:
    print('Total de {:.0f} cédulas de R$50'.format(n50))
if n20 > 0:
    print('Total de {:.0f} cédulas de R$20'.format(n20) if n20 > 0 else '')
if n10 >0:
    print('Total de {:.0f} cédulas de R$10'.format(n10) if n10 > 0 else '')
if n1 > 0:
    print('Total de {:.0f} cédulas de R$1'.format(n1) if n1 > 0 else '')
print('='*25)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')