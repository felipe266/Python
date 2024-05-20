#from utilitarius import *
#from banco_de_dados import *
from interface import *


menu()

#while True:
#    c = atualizar_categorias('receita')
#    c1 = atualizar_categorias('despesas')
#
#    mostra_saldo('banco')
#    mostrabanco('banco')
#    listas()
#    print('~~'*22)
    
#    esco = int(input('escolha uma categoria: '))
#    if esco == 0:
#        esco = c
#    elif esco == 1:
#        esco = c1
#    
#    m = atualizar_transacao(str(input('Observação: ').strip()),
#                        float(input('Valor: ').replace(',','.')),
#                        esco
#    )
#    '''nome = str(input('Nome do arquivo: '))
#    if arqexiste(nome) == False:
#        criar_arquivo(nome)'''
#    cadastrar(m.valor, m.categoria, m.descricao,arq='banco')
    
#    cont = str(input('Continuar: [S/N]: ').strip())
#    if cont in 'Nn':
#        break

#mostrabanco('banco')
#saldo_total()