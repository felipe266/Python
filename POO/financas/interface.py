from utilitarius import *
from banco_de_dados import *
from time import sleep

def linha(tam=45):
    print('='*tam)


def alinhamento(nome):
    linha()
    print(f'{nome}'.center(45))
    linha()

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
            


def menu():
    c = [atualizar_categorias('receita'), atualizar_categorias('despesas')]
    while True:
        alinhamento('Menu principal')
        opcao = ('ver transações', 'Total de saldo', 'Cadastrar transação', 'Sair do sistema')
        for n,op in enumerate(opcao):
            print(n+1,'-',op)
        linha()
        
        esco = erro_escolha(erro_int('Escolha uma opção: '),
                    len(opcao)
                )
        if esco == 1:
            alinhamento('Transações')
            mostra_banco('banco')
            sleep(1)
        if esco == 2:
            alinhamento('saldo disponivel')
            mostra_saldo('banco')
            sleep(1)
        if esco == 3:
            while True:
                alinhamento('cadastrar transação')
                for n, ca in enumerate(c):
                    print(n+1,'-', ca.nome)
                op = erro_escolha(erro_int('escolha uma categoria: '), len(c))
                
                m = atualizar_transacao(
                        str(input('Observação: ').strip()),
                        erro_float('Valor: '),
                        c[op-1]
                    )
                cadastrar(m.valor, m.categoria, m.descricao,arq='banco')
                con = str(input('deseja continuar? ').strip())
                if con in 'Nn':
                    break
            sleep(1)
        if esco == 4:
            alinhamento('Programa encerrado')
            break