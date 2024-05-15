#EXERCÍCIO 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:-IMC abaixo de 18,5: Abaixo do Peso-Entre 18,5 e 25: Peso Ideal-25 até 30: Sobrepeso-30 até 40: Obesidade-Acima de 40: Obesidade Mórbida
peso = str(input('seu peso? kg').strip())
peso = float(peso.replace(',','.'))
altura = str(input('sua altura[metros]? ').strip())
altura = float(altura.replace(',','.'))

imc = peso/(altura)**2

if imc < 18.5:
    print(f'seu imc é {imc:.2f} e estar abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'seu imc é {imc:.2f} e seu peso é ideal')
elif 25 <= imc < 30:
    print(f'seu imc é {imc:.2f} e está sobrepeso')
elif 30 <= imc < 40:
    print(f'seu imc é {imc:.2f} e está com obesidade')
elif imc >= 40:
    print(f'seu imc é {imc:.2f} e está com obesidade mórbida')
else:
    print('erro :(')

print('º~~'*20)

#EXERCÍCIO 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: -à vista dinheiro/cheque: 10% de desconto -à vista no cartão: 5% de desconto -em até 2x no cartão: preço formal -3xou mais no cartão: 20% de juros
valor = str(input('o preço do produto? ').strip())
valor = float(valor.replace(',','.'))
print('1-à vista dinheiro \n2-à vista cartão \n3-2x no cartão \n4-3x ou mais cartão: ')
mod = int(input('modo de pagamento? '))

if mod == 1:
    print(f'o valor {valor} com desconto de 10% é {valor*(1-0.1)}')
elif mod == 2:
    print(f'o valor {valor} com desconto de 5% é valor {valor*(1-0.05)}')
elif mod == 3:
    print(f'o valor {valor} não tem desconto')
elif mod == 4:
    print(f'o valor {valor} com jurus é {valor*(1+0.2)}')
else:
    print('erro :(')