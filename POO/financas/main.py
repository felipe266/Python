from utilitarius import(
    atualizar_categorias,
    atualizar_transacao,
    saldo_total,
    listas
)
from banco_de_dados import(
    criar_arquivo, 
    cadastrar,
    arqexiste
)


c = atualizar_categorias('receita')
c1 = atualizar_categorias('despesas')

listas()

while True:
    esco = int(input('escolha uma categoria: '))
    if esco == 0:
        esco = c
    elif esco == 1:
        esco = c1
    
    m = atualizar_transacao(str(input('Observação: ').strip()),
                        float(input('Valor: ')),
                        esco
    )
    nome = str(input('Nome do arquivo: '))
    if arqexiste(nome) == False:
        criar_arquivo(nome)
    cadastrar(m.valor, m.categoria, m.descricao,arq=nome)
    
    cont = str(input('Continuar: [S/N]: ').strip())
    
    if cont in 'Nn':
        break

saldo_total()