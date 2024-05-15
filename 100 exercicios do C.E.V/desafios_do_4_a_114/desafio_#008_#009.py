#EXERCÍCIO 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metros = float(input('um valor em metros: '))

centimetros = (metros * 100)
milimetros = (centimetros * 10)

print(f'o valor {metros} em centimetros {centimetros} e milimetros {milimetros}')

print('*~~'*20)

#EXERCÍCIO 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada
num = int(input('escolha um número: '))
escolha = int(input('0-somar|+ 1-subtrair|- 2-multiplicar|* 3-dividir|÷: '))
operacao = ('+', '-', '*', '/')

for n in range(1,11):
    print(f'{n} {operacao[escolha]} {num} =',end=' ')
    if operacao[escolha] == '+':
        print(n + num)
    if operacao[escolha] == '-':
        print(n - num)
    if operacao[escolha] == '*':
        print(n * num)
    if operacao[escolha] == '/':
        print(f'{(n / num):.3f}')