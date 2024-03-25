#EXERCÍCIO 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = str(input('qual a distância percorrida[Km]? '))
dist = float(dist.replace(',', '.'))

if dist <= 200:
    preco = 0.5 * dist
if dist > 200:
    preco = 0.45 * dist

print(f'A distância foi {dist} e passagem foi de {preco}')

print('*~~'*20)

#EXERCÍCIO 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = str(input('qual o ano? '))

dezena = int(ano[::-1][1])*10 + int(ano[::-1][0])
if dezena == 0:
    print(f'O ano {ano} não é bissexto')
if dezena != 0:
    if dezena%4 == 0:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')