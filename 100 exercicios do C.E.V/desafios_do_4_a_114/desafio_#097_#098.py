#EXERCÌCIO 97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(text):
    a = len(text)+4
    print('~'*a)
    print(f'  {text}')
    print('~'*a)


escreva('ola mundo')
escreva('Ola mestre felipe')

#EXERCÍCIO 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2c) uma contagem personalizada
def contador(ini, fim, pas):
    if fim >= ini:
        for n in range(ini, fim+1,pas):
            print(n,end=' ')
        print()
    elif ini >= fim:
        for n in range(ini, fim-1, -pas):
            print(n,end=' ')
        print()


print('Contagem de 1 até 10')
contador(1, 10, 1)
print('-='*15)
print('contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
print('-='*15)
print('personalize sua contagem')
contador(int(input('Início: ').strip()), int(input('Fim: ').strip()), int(input('Passo: ').strip()))