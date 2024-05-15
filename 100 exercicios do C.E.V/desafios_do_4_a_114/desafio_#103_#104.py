#EXERCÍCIO 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome ='<-desconhecido->', gol = 0):
    print(f'O jogador {nome} fez {gol} gol(s) na partida')


nome = str(input('Nome do jogador: ').strip())
gol = str(input('números de Gols: ').strip())

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome == '':
    ficha(gol=gol)
else:
    ficha(nome,gol)

print('~='*20)

#EXERCÍCIO 04: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.Ex: n = leiaInt('Digite um n: ')
def leiaint(num):
    n = input(num)
    while True:
        if n.isnumeric() == False:
            print('\033[0;31mERRO! DIGITE UM NÚMERO\033[m')
            n = input(f'{num}')
        else:
            num = int(n)
            break
    return num


num = leiaint('digite um número: ')
print(f'você digitou o número {num}')