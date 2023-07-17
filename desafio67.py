t = 'DESAFIO 67 Tabuada v.3.0 - break'
print(f'{t:=^105}')

while True:
    n = float(input('Quer ver a tabuada de qual valor? '))
    if n <= 0:
        break
    for c in range(1,11):
        s = n * c
        print(f'{n:.0f} x {c:.0f} = {s:.0f}')
print('Obrigado!')