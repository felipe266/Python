#EXERCÍCIO 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = s = 0
n = 1
print('999 para cancelar')
while num != 999:
    num = int(input(f'digite o {n} número: ').strip())
    if num != 999:
        s += num
    n += 1
print(f'a soma de todos os número digitados são {s}')

print('~='*20)

#EXERCÍCIO 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
c = 's'
s = 0
m = 0
while c not in 'Nn':
    num = int(input(f'digite o {m+1} valor: ').strip())
    c = str(input('Quer continuar[S/N]? ').strip())

    s += num
    m += 1
    if c in 'Nn':
        media = s /m
print(f'a média dos valores é {media}')