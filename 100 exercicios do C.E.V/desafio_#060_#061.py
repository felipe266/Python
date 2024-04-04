#EXERCÍCIO 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
num = int(input('digite um número para fatorar: ').strip())

fat = 1
for n in range(num,0,-1):
    print(f'{n} {'=' if n == 1 else 'x'}',end=' ')
    fat *= n
print(fat)

print('~='*20)

#EXERCÍCIO 61: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

num = int(input('1º termo da P.A: ').strip())
r = int(input('razão P.A: ').strip())

pa = n = 1
while pa != num + (9)*r:
    pa = num + (n-1)*r
    n += 1
    print(pa)