#EXERCÍCIO 74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('os números foram')
print(num)
print(f'O maior valor {max(num)} e o menor valor {min(num)}')

print('~='*20)

#EXERCÍCIO 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:A) Quantas vezes apareceu o valor 9.B) Em que posição foi digitado o primeiro valor 3.C) Quais foram os números pares.
num =(int(input('1º número: ').strip()),int(input('2º número: ').strip()),int(input('3º número: ').strip()),int(input('4º número: ').strip()))
m = c = p = par = 0
print('números pares são: ',end='')
for n in range(0,4):
    if num[n] == 9:
        m += 1
    if num[n] == 3 and c == 0:
        p = n
        c += 1
    if num[n]%2 == 0:
        print(num[n],end=' ')
print()
print(f'quantidade de 9 foi: {m}')
if c > 0:
    print(f'a 1º posiçao do 3 foi {p}')
elif c == 0:
    print('não tem 3')