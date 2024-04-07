#EXERCÍCIO 76: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('='*40)
print(f'{"Lista de produto":^40}')
print('='*40)
produto = ('lqpis',1.75, 'borracha',2, 'caderno',15.90, 'estojo',25, 'livro',34.9, 'caneta',22.3, 'mochila',120.32, 'sapato',110)
for n in range(0,16):
    if n%2 == 0:
        print(f'{produto[n]:.<30}',end='')
    if n%2 == 1:
        print(f'R$ {produto[n]:>6.2f}')

print('=~'*20)

#EXERCÍCIO 77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('ÁPRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMAR', 'FUTURO')

print('A' in palavras[0])

for n in range(0,len(palavras)):
    print(f'\nna palavra {palavras[n]} temos',end=' ')
    if 'A' in palavras[n]:
        print('a',end=' ')
    if 'E' in palavras[n]:
        print('e',end=' ')
    if 'I' in palavras[n]:
        print('i',end=' ')
    if 'O' in palavras[n]:
        print('o',end=' ')
    if 'U' in palavras[n]:
        print('u',end=' ')
#GUANABARA