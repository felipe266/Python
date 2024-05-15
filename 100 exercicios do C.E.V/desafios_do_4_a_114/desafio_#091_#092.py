#EXERCÍCIO 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
jogadores = {}
for n in range(0,4):
    m = jogadores[f'jogador{n+1}'] = randint(1,6)
    print(f'o jogador{n+1} tirou {m}')
    sleep(1)
rank = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
print('='*25)
print(f'{"  Ranking dos jogadores":^20}')
print('='*25)
m = 1
for c in rank:
    print(f'{m}º lugar: {c[0]} com {c[1]}')
    m += 1

print('-='*15)

#EXERCÍCIO 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
print(date.today().year)
pessoas = {
    'Nome': str(input('Nome: ').strip()),
    'idade': date.today().year - int(input('Ano de nascimento: ').strip()),
    'ctps': int(input('carteira de trabalho (0 não tem): ').strip())
}
if pessoas['ctps'] != 0:
    pessoas['contratação'] = int(input('Ano da contratação: ').strip())
    pessoas['salário'] = float(input('Salário: R$').strip().replace(',','.'))
    pessoas['aposentadoria'] = (67 - (pessoas['idade'] - (date.today().year-pessoas['contratação'])))
print('-='*15)
for k, v in pessoas.items():
    print(f'{k} tem o valor {v}')