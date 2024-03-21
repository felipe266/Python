#EXERCÍCIO 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
dinheiro = str(input('quanto de dinheiro? ').strip())
dinheiro = float(dinheiro.replace(',','.'))

dolar = (dinheiro/4.97)

print(f'com {dinheiro}R$ da para obter {dolar:.4f}$')

print('*~~'*20)

#EXERCÍCIO 11:Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
largura = str(input('qual a largura? ').strip())
altura = str(input('qual a altura? ').strip())
largura = float(largura.replace(',','.'))
altura = float(altura.replace(',','.'))

area = largura*altura
tinta = area/2

print(f'{largura} x {altura} da uma área de {area} e a tinra necessária é {tinta}L')