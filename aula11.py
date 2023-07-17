print('AULA 11 - CORES NO TERMINAL')
#\033[0;30;41m
#\033[4;33;44m
#\033[1;35;43m
#\033[30;42
#\033[m
#\033[7;30m

print('\033[4;30;45mOlá, mundo!\033[m')

nome = 'Winissius'
print('Olá, {}{}{}'.format('\033[4;34m',nome,'\033[m'))

cores = {'limpa':'\033[m'}

print('olá, {}{}'.format(cores(azul), nome))
