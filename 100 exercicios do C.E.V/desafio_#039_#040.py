#EXERCÍCIO 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('seu ano de nascimento? '))

idade = date.year() - ano

if idade < 18:
    print(f'sua idade é {idade} ainda vai se alistar')
elif idade > 18:
    print(f'sua idade é {idade} já passou do tempo')
elif idade == 18:
    print(f'sua idade é {idade} já esta hora de alistar')
else:
    print('erro :(')

print('º~~'*20)

#EXERCÍCIO 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÃO - Média 7.0 ou superior: APROVADO
nota1 = str(input('1º nota: '))
nota1 = float(nota1.replace(',','.'))
nota2 = str(input('1º nota: '))
nota2 = float(nota2.replace(',','.'))

media = (nota1 + nota2)/2

if media < 5:
    print(f'sua média foi {media} e foi reprovado')
elif 7 < media >= 5:
    print(f'sua média foi {media} e foi de recuperação')
elif media > 7:
    print(f'sua média foi {media} e foi aprovado')
else:
    print('erro :(')