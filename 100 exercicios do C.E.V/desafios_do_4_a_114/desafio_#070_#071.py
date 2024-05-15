#EXERCÍCIO 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:A) qual é o total gasto na compra.B) quantos produtos custam mais de R$1000.C) qual é o nome do produto mais barato.
print('Cadastro de produtos')
print('~='*15)

s = custo = menor = menor_p = n = 0
while True:
    nome = str(input('Nome: ').strip())
    preco = str(input('Preço: R$').strip().lower())
    preco = float(preco.replace(',','.'))
    cont = str(input('Continuar? [S/N] ').strip().lower())
    print('=+'*10)

    s += preco
    if preco > 1000:
        custo += 1
    if n == 0:
        menor = preco
        menor_p = nome
    if preco <= menor:
        menor = preco
        menor_p = nome
    n = 1
    if cont in 'Nn':
        break

print(f'Total gasto: {s}')
print(f'produtos maiores de 1000: {custo}')
print(f'o produto mais barato é {menor_p} e custa {menor}R$')

print('~='*20)

#EXERCÍCIO 71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
preco = int(input('Valor à sacar: R$').strip())

#MEU MODO
ciquenta = int(preco/50)
preco = preco - (ciquenta*50)
if ciquenta != 0:
    print(f'total de {ciquenta} cedulas de R$50')
vinte = int(preco/20)
preco = preco - (vinte*20)
if vinte != 0:
    print(f'total de {vinte} cedulas de R$20')
dez = int(preco/10)
preco = preco - (dez*10)
if dez != 0:
    print(f'total de {dez} cedulas de R$10')
um = int(preco/1)
if um != 0:
    print(f'total de {um} cedulas de R$50')

#MODO GUANABARA
total = preco
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cedulas de {ced}R$')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break