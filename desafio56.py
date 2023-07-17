t = 'DESAFIO 56 - ANALISAR COMPLETO (FOR)'
print('{:=^105}'.format(t))

soma = 0
iM = 0
nM = 0
iF = 0
F = 0
M = 0
for c in range(1,5):
    print(30*'=')
    print('{}º PESSOA'.format(c))
    n = str(input('Qual sua graça? ')).upper().strip()
    i = int(input('Qual sua idade? '))
    s = str(input('Qual seu sexo F/M: ')).upper().strip()

    if c==1:
        soma = i
        if s == str('M'):
            nM = n
            iM = i
            M += 1
    else:
        soma += i
        if s == 'M' and i > iM:
            iM = i
            nM = n
    if s == 'F' and i < 20:
        F += 1
    if s == 'M' and c != 1:
        M += 1
    med = (soma)/c

print('A média da idade do grpo é {} anos'.format(med))
if M > 0:
    print('O nome do homem mais velho é {} e sua idade é {} anos'.format(nM,iM))
else:
    print('Não há homens no grupo')
print('Ao todo são {} mulheres menores de 20 anos'.format(F))