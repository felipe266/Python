#EXERCÍCIO 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('seu nome: ').strip())
nome = nome.split()

print(f'seu 1º nome: {nome[0]} \nultimo nome:{'não tem'if nome[len(nome)-1] == nome[0] else nome[len(nome)-1] }')

print('*~~'*20)

#EXERCÍCIO 28: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

num = int(input('esolha um número de (0 à 5): '))
print('um momento o computado está pensando')
for n in range(0,4):
    sleep(1)
    print('.')
escolhido = randint(0, 5)

if escolhido == num:
    print(f'PARABÉNS o número foi {escolhido} você ganhou')
else:
    print(f' o número escolhido foi {escolhido} que pena você errou')