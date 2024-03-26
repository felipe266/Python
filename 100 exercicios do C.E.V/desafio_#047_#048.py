#EXERCÍCIO 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
from time import sleep
print('todos os números pares entre 1 à 50')
for n in range(0,51,2):
    print(n)
    sleep(0.5)

print('º~~'*20)

#EXERCÍCIO 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
print('soma dos múltiplos de 3')

s = 0
for n in range(1,501):
    if n%3 == 0:
        print(n)
        s += n
print(f'a soma deu {s}')