#EXERCÍCIO 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:- Até 9 anos: MIRIM- Até 14 anos: INFANTIL- Até 19 anos: JÚNIOR- Até 25 anos: SÊNIOR- Acima de 25 anos: MASTER
from time import sleep
atletas = {}
inscrito = []
while True:
    atletas['Nome'] = str(input('Nome: ').strip())
    atletas['Idade'] = int(input('idade: ').strip())
    
    if atletas['Idade'] <= 9:
        atletas['categoria'] = 'Mirim'
    elif 9 < atletas['Idade'] <= 14:
        atletas['categoria'] = 'Infantil'
    elif 14 < atletas['Idade'] <= 19:
        atletas['categoria'] = 'júnior'
    elif 19 < atletas['Idade'] <= 25:
        atletas['categoria'] = 'Master'
    
    inscrito.append(atletas.copy())
    
    cont = str(input('deseja continuar[S/N]: '))
    
    if cont in 'nN':
        break

print('=-'*12)

for p in inscrito:
    for k, v in p.items():
        print(f'{k}: {v}')
    sleep(1)

print('º~~'*20)

#EXERCÍCIO 42: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:-EQUILÁTERO: todos os lados iguais-ISÓSCELES: dois lados iguais, um diferente-ESCALENO: todos os lados diferentes
l1 = str(input('1º lado do triângulo[cm]: ').strip())
l1 = float(l1.replace(',', '.'))
l2 = str(input('1º lado do triângulo[cm]: ').strip())
l2 = float(l2.replace(',', '.'))
l3 = str(input('1º lado do triângulo[cm]: ').strip())
l3 = float(l3.replace(',','.'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 and l2 == l3:
        print(f'as medidas {l1}cm, {l2}cm e {l3}cm formam um triângulo equilátero')
    if l1 == l2 and l1 != l3:
        print(f'as medidas {l1}cm, {l2}cm e {l3}cm formam um triângulo isósceles')
    if l1 == l3 and l2 != l3:
        print(f'as medidas {l1}cm, {l2}cm e {l3}cm formam um triângulo isósceles')    
    if l2 == l3 and l2 != l1:
        print(f'as medidas {l1}cm, {l2}cm e {l3}cm formam um triângulo isósceles')
    if l1 != l2 and l1 != l3 and l2 != l3:
        print(f'as medidas {l1}cm, {l2}cm e {l3}cm formam um triângulo escaleno')
else:
    print(f'as medidas {l1}cm, {l2}cm e {l3}cm não formam um triângulo')