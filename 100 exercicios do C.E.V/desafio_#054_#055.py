#EXERCÍCIO 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

hoje = date.today().year
menor = 0
for n in range(0,7):
    ano = int(input(f'em que ano o {n+1}º nasceu: '))
    idade = hoje - ano
    if idade < 18:
        menor += 1

print(f'a quantidade de pessoa menores de idade é {menor}')

print('*=='*20)

#EXERCÍCIO 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
for n in range(0,7):
    peso = str(input(f'qual o peso do {n+1}º Kg ').strip())
    peso = float(peso.replace(',','.'))
    
    if n == 0:
        menor = maior = peso
    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso

print(f'o menor peso é {menor}')
print(f'o maior peso é {maior}')