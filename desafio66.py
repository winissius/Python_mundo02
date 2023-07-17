t = 'DESAFIO 66 - FLAGS COM BREAK'
print(f'{t:=^105}')

s = c = 0
while True:
    n = int(input('Digite um valor [999 par parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores foi {s}!')