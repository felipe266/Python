#EXERCÍCII 82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
numeros = list()
pares = list()
impares = list()
n = 1
while True:
    numeros.append(int(input(f'O {n} número: ').strip()))
    cont = str(input('quer continuar? [S/N]').strip())
    n += 1
    if cont in 'nN':
        break

for m in range(0,len(numeros)):
    if numeros[m]%2 == 0:
        pares.append(numeros[m])
    elif numeros[m]%2 == 1:
        impares.append(numeros[m])

print(f'Todos os números são {numeros.sort()}')
print(f'os números pares {pares.sort()}')
print(f'os números impares {impares.sort()}')

print('~=='*15)

#EXERCÍCIO 83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expre = str(input('Digite uma expressão: ').strip().lower())
d = i = 0
for l in expre:
    if l == '(':
        d += 1
    elif l == ')':
        i += 1

s = d - i
if s < 0 or s > 0:
    print('expressão está errada')
elif s == 0:
    print('expressão está certa')