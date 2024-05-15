#EXERCÍCIO 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = str(input('qual o preço? ').strip())
preco = float(preco.replace(',','.'))

new_preco = preco*(1 - 0.05)

print(f'o valor de {preco} com desconto de 5% é {new_preco}')

print('²~~'*20)

#EXERCÍCIO 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = str(input('seu salário? ').strip())
salario = float(salario.replace(',','.'))

new_salario = salario*(1 + 0.15)

print(f'o salário de {salario} com aumento de 15% fica {new_salario}')