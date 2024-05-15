#EXERCÍCIO 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('qaul seu número: '))

binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)

print(f'o número {num} em \nbinário: {binario} \noctal: {octal} \nhexadecimal: {hexadecimal}')

print('º~~'*20)

#EXECÍCIO 38: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: - O primeiro valor é maior - O segundo valor é maior - Não existe valor maior, os dois são iguais
num1 = str(input('1º número: '))
num1 = float(num1.replace(',','.'))
num2 = str(input('1º número: '))
num2 = float(num2.replace(',','.'))

if num1 > num2:
    print(f'{num1} > {num2}')
elif num2 > num1:
    print(f'{num2} > {num1}')
elif num1 == num2:
    print(f'{num1} = {num2}')