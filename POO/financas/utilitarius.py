from transacao import Transacao
from categoria import Categoria


lista_transacao = []
lista_categorias = []

def atualizar_transacao(descricao,valor,categoria):
    nova_transacao = Transacao(descricao,valor,categoria)
    lista_transacao.append(nova_transacao)
    return nova_transacao


def atualizar_categorias(nome):
    nova_categoria = Categoria(nome)
    lista_categorias.append(nova_categoria)
    return nova_categoria


def saldo_total():
    saldo = 0
    for t in lista_transacao:
        valor = t.valor
        if t.categoria.nome == 'despesas':
            saldo -= valor
        else:
            saldo += valor
    print(f'O saldo total ficou {saldo}')


def listas():
    print('Listas de categorias:')
    for n,l in enumerate(lista_categorias):
        print(f' {n} - {l.nome}')


def erro_int(text):
    while True:
        try:
            n = int(input(text))
        except (TypeError,ValueError):
            print('\033[0;31mErro número inválido\033[m')
        else: 
            return n


def erro_float(text):
    while True:
        try:
            n = float(input(text))
        except (TypeError,ValueError):
            print('\033[0;31mErro número inválido\033[m')
        else: 
            return n


def erro_escolha(num, tam):
    while True:
        if num > tam or num < 1:
            print('\033[0;31mErro número não condiz com as opções\033[m')
            num = erro_int('Escolha uma opção: ')
        else:
           return num