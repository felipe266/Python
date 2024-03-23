#EXERCÍCIO 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velo = str(input('qual a velocidade em km/h? '))
velo = float(velo.replace(',', '.'))

if velo > 80:
    multa = (velo - 80)*7
    print(f'você ultrapassou o limite de 80km/h sum multa será {multa}R$')
else:
    print(f'sua velocidade é {velo} parabéns')

print('*~~'*20)

#EXECÍCIO 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('escolha um número inteiro: ').strip())

if num % 2 == 0:
    print(f'o número {num} é par')
if num % 2 == 1:
    print(f'o número {num} é impar')
else:
    print('ERRO')