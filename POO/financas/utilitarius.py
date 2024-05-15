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