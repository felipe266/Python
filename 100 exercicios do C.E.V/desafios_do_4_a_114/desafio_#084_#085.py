#EXERCÍCIO 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas.B) Uma listagem com as pessoas mais pesadas.C) Uma listagem com as pessoas mais leves.
pessoas = []
temp = []
c = t = max = min = 0
while True:
    temp.append(str(input('Nome: ').strip()))
    temp.append(float(input('Peso: ').strip().replace(',','.')))
    pessoas.append(temp[:])
    temp.clear()
    if c == 0:
        max = min = pessoas[c][1]
    else:
        if pessoas[c][1] >= max:
            max = pessoas[c][1]
        elif pessoas[c][1] <= min:
            min = pessoas[c][1]
    cont = str(input('quer continuar? [S/N]').strip())
    if cont in 'nN':
        break
    c += 1
print(f'quantidade de pessoas cadastrada {len(pessoas)}')

print(f'O peso maias pesado foi {max} e são das pessoas:', end=' ')
for n in range(0,len(pessoas)):
    if pessoas[n][1] == max:
        print(f'[{pessoas[n][0]}]', end=' ')
print(f'\nO peso maias pesado foi {min} e são das pessoas:', end=' ')
for n in range(0,len(pessoas)):
    if pessoas[n][1] == min:
        print(f'[{pessoas[n][0]}]', end=' ')

print('~='*20)

#EXERCÍCIO 85: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
for n in range(0,7):
    num = int(input('Digite um número: '))
    if num%2 == 0:
        numeros[0].append(num)
    elif num%2 == 1:
        numeros[1].append(num)

print(f'Os números pares são: {numeros[0]}')
print(f'os números imapres são: {numeros[1]}')