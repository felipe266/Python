#EXERCÍCIO 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
num = int(input('digite um número de 0 à 10: ').strip())

print(f'você digitou o número {extenso[num]}')

print('~='*15)

#EXERCÍCIO 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:a) Os 5 primeiros times.b) Os últimos 4 colocados.c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.
tabela = ('corintia','botafogo','ceara','fortaleza','flamego','sao paulo','bahia','fluminense','santos','palmeira')
print('Os 5 primeiros times')
for n in range(0,5):
    print(tabela[n])
print('Os últimos 4 colocados')
for m in range(9,5,-1):
    print(tabela[m])
print('Times em ordem alfabética')
print(sorted(tabela))