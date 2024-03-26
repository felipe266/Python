#EXERCÍCIO 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print('1-pedra \n2-tesoura \n3-papel')
escolha = int(input('qual sua escolha? ').strip())

comp = randint(1,3)
print(comp)

if escolha == 1 and comp == 2:
    print('Parabêns você ganhou')
elif escolha == 2 and comp == 3:
    print('Parabêns você ganhou')
elif escolha == 3 and comp == 1:
    print('Parabêns você ganhou')
elif escolha == comp:
    print('Empate')
else:
    print('você perdeu')

print('º~~'*20)

#EXERCÍCIO 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Preste atenção a bomba vai estourar em 10s')

for n in range(1,11):
    print(f'💣{n}...')
    sleep(1)

print('bummmmmmmmmmmmmmmm🧨🔥')