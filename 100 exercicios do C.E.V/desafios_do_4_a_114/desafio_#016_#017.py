#EXERCÍCIO 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
num = str(input('um número? ').strip())
num = float(num.replace(',', '.'))

print(f'o número {num} inteiro é {int(num)}')

print('²~~'*20)

#EXERCÍCIO 17:Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
cat_opos = str(input('cateto oposto: ').strip())
cat_opos = float(cat_opos.replace(',', '.'))
cat_adj = str(input('cateto oposto: ').strip())
cat_adj = float(cat_adj.replace(',', '.'))

hipo = ((cat_opos**2) + (cat_adj**2))**(1/2)

print(f'{cat_opos}² + {cat_adj}² = {hipo:.3f}²')