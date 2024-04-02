#EXERCÍCIO 58: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
from random import randint

num = int(input('escolha um número de 0 à 10: ').strip())

print('Um momento o computador está pensando')
for n in range(0,4):
    print(f'{n+1}.')
    sleep(1)
escolhido = randint(0,10)

q = 1
while escolhido != num:
    print('Você errou ')
    num = int(input('escolha outro número: '))
    q += 1
print('~='*15)
print('Parabéns você acertou')
print(f'a quantidade de tentativas é {q}')

print('~='*20)

#EXERCÍCIO 59: Crie um programa que leia dois valores e mostre um menu na tela:[ 1 ] somar[ 2 ] multiplicar[ 3 ] maior[ 4 ] novos números[ 5 ] sair do programa Seu programa deverá realizar a operação solicitada em cada caso.

num1 = str(input(f'escolha 1º número: '))
num1 = float(num1.replace(',','.'))
num2 = str(input(f'escolha 2º número: '))
num2  = float(num2.replace(',','.'))

escolha = 0
while escolha != 5:
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair')
    escolha = int(input('escolha uma opereção: '))

    if escolha == 1:
        print(f'o resultado de {num1} + {num2} é {num1 + num2}')
        print('~='*10)
    elif escolha == 2:
         print(f'o resultado de {num1} * {num2} é {num1 * num2}')
         print('~='*10)
    elif escolha == 3:
        if num1 > num2:
             print(f'o maior é {num1}')
             print('~='*10)
        else:
            print(f'o maior é {num2}')
            print('~='*10)
    elif escolha == 4:
        num1 = str(input(f'escolha 1º número: '))
        num1 = float(num1.replace(',','.'))
        num2 = str(input(f'escolha 2º número: '))
        num2  = float(num2.replace(',','.'))
        print('~='*10)
print('FIM')