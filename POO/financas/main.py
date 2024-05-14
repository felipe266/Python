from utilitarius import(
    atualizar_categorias,
    atualizar_transacao,
    saldo_total
)


c = atualizar_categorias('receita')
c1 = atualizar_categorias('despesas')

atualizar_transacao('salário', 5000, c)
atualizar_transacao('viagem', 600, c1)
atualizar_transacao('comida', 350, c1)
atualizar_transacao('mesada', 100, c)

print(saldo_total())