#EXERCÍCIO 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []
numeros_ord = []
m = p = 0
for n in range(0,5):
    numeros.append(int(input(f'o {n+1}º número: ').strip()))

for m in range(0,len(numeros)):
    for n in range(0,len(numeros)):
        if numeros[m] < numeros[n]:
            p = numeros[m]
            numeros[m] = numeros[n]
            numeros[n] = p
print(numeros)

print('~='*15)

#EXERCÍCIO 81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados.B) A lista de valores, ordenada de forma decrescente.C) Se o valor 5 foi digitado e está ou não na lista.
numeros = list()
n = 0
while True:
    numeros.append(int(input(f'O {n+1} número: ').strip()))
    cont = str(input('quer continuar? [S/N]').strip())
    n += 1
    if cont in 'nN':
        break

print(f'Quantidade de números digitados são {n}')
print('em ordem decrescente',end=': ')
for m in range(0,len(numeros)):
    for n in range(0,len(numeros)):
        if numeros[m] > numeros[n]:
            p = numeros[m]
            numeros[m] = numeros[n]
            numeros[n] = p
print(numeros)
if 5 in numeros:
    print('5 está na lista')
else:
    print('5 não está na lista')