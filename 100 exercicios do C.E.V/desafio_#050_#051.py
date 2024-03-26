#EXERCÍCIO 49:JA FOI FEITO NO DESAFIO 9
#EXERCÍCIO 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
for n in range(0,6):
    num = int(input(f'o {n+1}º número: ').strip())
    if num%2 == 0:
        s += num
print(f'a soma dos pares é {s}')

#EXERCÍCIO 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
num = int(input('1º termo da P.A: ').strip())
r = int(input('razão P.A').strip())

t = 1
for n in range(num, num +(11-1)*r, r):
    print(f'{t}º: {n}')
    t += 1