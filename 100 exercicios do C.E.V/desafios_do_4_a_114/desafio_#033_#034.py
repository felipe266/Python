#EXERCÍCIO 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = str(input('um número? ').strip())
a = float(a.replace(',', '.'))
b = str(input('um número? ').strip())
b = float(b.replace(',', '.'))
c = str(input('um número? ').strip())
c = float(c.replace(',', '.'))

if a > b and a > c:
    print(f'o {a} é o maior')
elif b > a and b > c:
    print(f'o {b} é o maior')
elif c > a and c > b:
    print(f'o {c} é o maior')

print('º~~'*20)

#EXERCÍCIO 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = str(input('seu salário[R$]? '))
salario = float(salario.replace(',','.'))

if salario > 1250:
    aumento = salario*(1 + 0.1)
    print(f'seu salário {salario} com aumento de 10% é {aumento:.3f}')
if salario <= 1250:
    aumento = salario*(1 + 0.15)
    print(f'seu salário {salario} com aumento de 15% é {aumento:.3f}')