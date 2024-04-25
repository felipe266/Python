#EXERCÍCIO 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
#EXERCÌCIO 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função inputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
from utilidadesCev import moeda, dado

p = dado.leiaDinheiro('Digite um preço: R$'
)
print('-='*20)
moeda.resumo(p,20,12)

print('~='*20)