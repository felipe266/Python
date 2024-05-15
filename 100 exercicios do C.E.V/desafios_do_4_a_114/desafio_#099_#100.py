#EXERCÌCIO 99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
    maior = 0
    for n in range(0,len(num)):
        print(num[n],end=' ')
        if n == 0:
            maior = num[n]
        else:
            if num[n] >= maior:
                maior = num[n]
    print(f'foram informados {len(num)} valores')
    print(f'O maior valor informado foi {maior}')
    print('-='*15)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

#EXERCÍCIO 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint


def sorteia(lista):
    print(f'Sorteando 5 números da lista: ',end='')
    for cont in range(0,5):
        n = randint(0,10)
        lista.append(n)
        print(n,end=' ')
    print()


def somapar(nu):
    sp = 0
    for n in nu:
        if n%2 == 0:
            sp += n
    print(f'somando os valores pares de {nu}, temos {sp}')


nums = []
sorteia(nums)
somapar(nums)