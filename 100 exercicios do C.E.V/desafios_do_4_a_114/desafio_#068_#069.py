#EXERCÍCIO 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('jogo de par ou impar(0 à 10)')
print('digite um número negativo para parar')
print('=¬'*20)

v = d = 0
while True:
    num = int(input('Digite um valor? ').strip())
    if num < 0:
        break
    esco = str(input('Par ou Impar? [P/I] ').strip().lower())
    print('=~'*20)

    num2 = randint(0,10)
    soma = num + num2

    print(f'Você jogou {num} e o computador {num2}')
    print('~~'*20)

    if esco == 'p':
        if soma%2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            d += 1
    elif esco == 'i':
        if soma%2 != 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            d += 1

print(f'Você ganhou {v} e o computador {d}')

print('~='*20)

#EXERCÍCIO 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos.B) quantos homens foram cadastrados.C) quantas mulheres tem menos de 20 anos.
maior = menor_m = h = 0 
while True:
    idade = int(input('Sua idade? ').strip())
    sexo = str(input('Sue sexo? [M/F] ').strip().lower())
    cont = str(input('quer continhuar? [S/N] ').strip().lower())
    print('=+'*20)

    if idade > 18:
        maior += 1
    if sexo == 'm':
        h += 1
    if sexo == 'f' and idade < 20:
        menor_m += 1
    
    if cont == 'n':
        break

print(f'Pessoas maiores de 18: {maior}')
print(f'Homens cadastrado: {h}')
print(f'Mulheres menores de 20: {menor_m}')