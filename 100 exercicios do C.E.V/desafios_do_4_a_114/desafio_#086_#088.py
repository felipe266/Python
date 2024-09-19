#EXERCÍCIO 86 e 87: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta, mostrando no final: A) A soma de todos os valores pares digitados.B) A soma dos valores da terceira coluna.C) O maior valor da segunda linha.
matriz = [[],[],[]]
sp = sc = sl = max = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(float(input(f'valor para [{l}, {c}]: ').strip().replace(',','.')))
        if matriz[l][c]%2 == 0:
            sp += matriz[l][c]
        if c == 2:
            sc += matriz[l][c]
        if l == 1:
            if matriz[l][c] >= max:
                max = matriz[l][c]

print('='*15)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end=' ')
        if c == 2:
            print()

print('='*15)
print(f'a soma de todos os pares são: {sp}')
print(f'a soma dos valores da 3 coluna: {sc}')
print(f'o maior valor da 2 linha: {max}')

print('~='*15)

#EXERCÍCIO 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
quant = int(input('Quantos jogos quer ver? ').strip())
jogos = []
temp = []
for n in range(0,quant):
    for m in range(0,6):
        temp.append(randint(0,60))
    jogos.append(temp[:])
    temp.clear()

print(f'-=-=-=-=-=-= Boa sorte -=-=-=-=-=-=')
for n in range(0,quant):
    print(f'Jogo {n+1}: {jogos[n]}')
    sleep(1)