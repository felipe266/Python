#EXERCÍCIO 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
l1 = str(input('1º lado do triângulo[cm]: ').strip())
l1 = float(l1.replace(',', '.'))
l2 = str(input('1º lado do triângulo[cm]: ').strip())
l2 = float(l2.replace(',', '.'))
l3 = str(input('1º lado do triângulo[cm]: ').strip())
l3 = float(l3.replace(',','.'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'as medidas {l1}cm, {l2}cm e {l3}cm formam um triângulo')
else:
    print(f'as medidas {l1}cm, {l2}cm e {l3}cm não formam um triângulo')

print('º~~'*20)

#EXERCÍCIO 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor = str(input('preço da casa[R$]? '))
valor = float(valor.replace(',','.'))
salario = str(input('seu salário[R$]? '))
salario = float(salario.replace(',','.'))
anos = int(input('em quantos anos vai pagar: '))

prestacao = (valor/(anos*12))
if prestacao > salario*(0.3):
    print(f'A prestação será de {prestacao:.2f} empréstimo negado')
else:
    print('Emprestimo confirmado')