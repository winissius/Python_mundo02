t = 'DESAFIO 59 - CÁLCULO DO FATORIAL (WHILE)'
print('{:=^105}'.format(t))

n = int(input('Digite um valor para descobrir seu fatorial: '))

#solução com while
'''f = 1

while n > 1:
    f = f * n
    n = n - 1
    if n == 0:
        f = 1
print('{}'.format(f))
'''

#solução com for
c = n
f = 1
for c in range (n, 0,-1):
    f *=c
print(f)