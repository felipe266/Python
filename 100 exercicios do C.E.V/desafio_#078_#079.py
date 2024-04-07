#EXERCÍCIO 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
numeros = {}
max = min = nmax = nmin = 0
for n in range(0,5):
    numeros[n] = float(input(f'o {n+1} número: ').strip())
    if n == 0:
        max = numeros[n]
        min = numeros[n]
    else:
        if numeros[n] >= max:
            max = numeros[n]
            nmax = n
        elif numeros[n] <= min:
            min = numeros[n]
            nmin = n
print(f'o mario número é {max} e sua posição é {nmax+1}')
print(f'o mario número é {min} e sua posição é {nmin+1}')

print('~='*20)

#EXERCÍCIO 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = []
n = 1
while True:
    num = int(input(f'digite o {n}º número: ').strip())
    if num not in numeros:
        numeros.append(num)
        print('valor cadastrado com sucesso')
    elif num in numeros:
        print('valor ja existe')
    con = str(input('Quer continuar?[S/N] ').lower().strip())
    if con in 'Nn':
        break
    n += 1
print(f'os números digitados em ordem crescente são {sorted(numeros, key=int)}')