#EXERCÍCIO 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        print(f'com {idade}: foi negado!')
        print('-='*15)
    elif 16 <= idade < 18:
        print(f'com {idade}: voto opcional')
        print('-='*15)
    elif idade >= 18:
        print(f'com {idade}: voto obrigaório')
        print('-='*15)


while True:
    voto(int(input('Ano de nascimento? ').strip()))
    con = str(input('continuar? [S/N]').strip())

    if con in 'nN':
        break

print('~='*20)

#EXERCÍCIO 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num,show):
    """
    fatorial(num,show=false)
    ->calcular o fatorial de um número:
        :param num: o número
        :param show: (opcional) mostra ou nao a conta
    """
    fat = 1
    print(show)
    for n in range(num,0,-1):
        if show == 'true':
            print(f'{n} {'x'if n > 1 else '='}', end=' ')
        fat *= n
    print(fat)


help(fatorial)
fatorial(int(input('1 número: ').strip()),str(input('true para mostrar a multiplicação false só para o resultado: ').lower()))