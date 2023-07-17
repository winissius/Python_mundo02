t = 'DESAFIO 48 - SOMA DE NÚMEROS IMPARES EM INTERVALO'
print('{:=^105}'.format(t))

soma = 0 # acumulador
cont = 0 # contador
for n in range (1,501):
    if n %2 !=0 and n %3 == 0:
        #print(n, end=' ')
        soma += n
        cont += 1
print("A soma dos {} é {}".format(cont,soma))