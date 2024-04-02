#EXERCÍCIO 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
menores = 0
first = 1
for n in range(0,4):
    print(f'~~~~~ {n+1}º PESSOA ~~~~~')
    nome = str(input('nome: ').strip())
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ').strip().lower())

    media += idade/4
    if sexo == 'm':
        if first == 1:
            maior = idade
            hmaior = nome
            first -= 1
        if idade >= maior:
            maior = idade
            hmaior = nome
    if sexo == 'f' and idade < 20:
        menores += 1

print(f'A média da do grupo é {media}')
print(f'A idade do homem mais velho {maior} e o nome {hmaior} ')
print(f'quantidade de mulheres menores de 20 é {menores}')

print('~~*'*20)

#EXERCÍCIO 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('qual seu sexo[M/F]: '))

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Informe seu sexo: '))