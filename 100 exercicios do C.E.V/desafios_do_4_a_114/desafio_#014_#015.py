#EXERCÍCIO 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
t_c = str(input('temperatura em celsius Cº: ').strip())
t_c = float(t_c.replace(',', '.'))

t_f = (t_c*(9/5)) + 32

print(f'a tempreta {t_c}Cº em fahrenheit é {t_f:.3f}Fº')

print('²~~')

#EXERCÍCIO 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
tabela = {}
km = str(input('quantidade de Km percorridos? ').strip())
tabela['km pecorrido'] = float(km.replace(',','.'))
tabela['dias pecorrido'] = int(input('quantidade de dias? ').strip())

preco = 0
for k, v in tabela.items():
    if k == 'km pecorrido':
        preco += 0.15*v
    if k =='dias pecorrido':
        preco += 60*v
        tabela['preço'] = preco
for k,v in tabela.items():
    print(f'{k} é {v}')