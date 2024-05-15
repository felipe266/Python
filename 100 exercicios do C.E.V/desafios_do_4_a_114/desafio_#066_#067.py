#EXERCÍCIO 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
print('Digite 999 para parar')
s = n = num = 0
while True:
    num = int(input(f'O {n+1}º número? ').strip())
    if num == 999:
        break
    s += num
    n += 1
print(f'a quantidade de número foi {n} e a soma é {s}')

print('~='*20)

#EXERCÍCIO 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
print('Digite um número negativo para parar')
while True:
    num = int(input('a tabuada sera de? ').strip())
    if num < 0:
        break
    for n in range(1,11):
        print(f'{n} x {num} = {n*num}')
    print('=+'*10)
print('FIM')