#EXERCÍCIO 95: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []
jogador = {}
gols = []

while True:
    sgols = 0
    jogador['nome'] = str(input('Nome: ').strip().lower())
    partidas = int(input('Quantos partidas: ').strip())
    for n in range(0,partidas):
        gols.append(int(input(f'Qantos gols na {n+1}º partida? ').strip()))
        sgols += gols[n]
    jogador['gols'] = gols[:]
    jogador['total'] = sgols
    gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    cont = str(input('Quer continuar?[S/N] ').strip())
    while cont not in 'SsNn':
        print('ERRO!, SO DIGITE [S/N]')
        cont = str(input('Quer continuar? ').strip())
    
    print('-='*15)
    
    if cont in 'Nn':
        break

print('Nº.Nome          gols        total')
print('='*35)
c = 0
for i in jogadores:
    print(f"{c:>2}  ",end='')
    for j in i.values():
        print(f'{str(j):<13}',end='')
    print()
    c += 1
print('='*35)

while True:
    num = int(input('Mostrar dados de qual jogador? (999 para)').strip())

    if num == 999:
        break
    
    while num > len(jogadores)-1 or num < 0:
        print('ERRO, não existe essa pessoas')
        num = int(input('Mostrar dados de qual jogador? (999 para)').strip())
    
    print(f'== levantamento do {str(jogadores[num]['nome']).upper()} ==')
    c = 1
    for n in jogadores[num]['gols']:
        print(f'   No jogo {c} fez {n}.')
    print('~=='*20)


#EXERCÍCIO 96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(a,b):
    print(f'as dimensão {a} x {b} dão uma aréa de {a*b}')


area(int(input('Largura: ').strip()), int(input('Comprimento: ')))