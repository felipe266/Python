#EXERCÌCIO 97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(text):
    a = len(text)+4
    print('~'*a)
    print(f'  {text}')
    print('~'*a)


escreva('ola mundo')
escreva('Ola mestre felipe')

#EXERCÍCIO 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1b) de 10 até 0, de 2 em 2c) uma contagem personalizada