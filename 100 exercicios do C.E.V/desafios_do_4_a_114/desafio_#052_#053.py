#EXERCÍCIO 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Um número entre 1 à 100: ').strip())

c = 0
print(f'o númuero {num} é divisivel por')
for n in range(1,101):
    if num%n == 0:
        c += 1
        print(f'{n}',end=' ')
print()
if c > 2:
    print('não é primo')
else:
    print('é primo')

print('*~~'*20)

#EXERCÍCIO 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
print('Descobrindo se é palidromo')
print('=+'*15)

palavra = str(input('digite um frase ai: '))
palavra = palavra.replace('',' ').strip().split()

c = 0
pa = 0
for p in range(len(palavra)-1,-1,-1):
    if palavra[p] == palavra[c]:
        print(palavra[p])
        print(palavra[c])
        pa += 1
        c += 1
if pa == len(palavra):
    print('A frase é um palidromo')
else:
    print('não é palidromo')