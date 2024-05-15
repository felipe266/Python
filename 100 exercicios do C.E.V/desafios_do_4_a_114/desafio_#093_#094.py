#EXERCÍCIO 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {
    'Nome': str(input('Nome: ').strip()),
    'partidas': int(input('quantas partidas? ').strip()),
}
gols = []
sg = 0
for g in range(0,jogador['partidas']):
    gols.append(int(input(f'quantos gols na {g+1} partida? ').strip()))
    sg += gols[g]
jogador['gols'] = gols
jogador['quantidade de gols'] = sg
print('-='*20)
for k,v in jogador.items():
    print(f'{k} tem o valor {v}')

print('~='*20)

#EXERCÍCIO 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoas em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradasB) A média de idadeC) Uma lista com as mulheresD) Uma lista de pessoas com idade acima da média
info = {}
pessoas = []
cad = si = 0
while True:
    info.clear()
    info['nome'] = str(input('Nome: ').strip())
    info['sexo'] = str(input('Sexo: [M/F]').strip().lower())
    while info['sexo'] not in 'mf':
        print('ERRO! digite apenas M OU F')
        info['sexo'] = str(input('Sexo: [M/F]').strip().lower())
    info['idade'] = int(input('Idade: ').strip())
    pessoas.append(info.copy())
    cont = str(input('Quer continuar? [S/N] ').strip().lower())
    while cont not in 'sn':
        print('ERRO! digite apenas S ou N')
        cont = str(input('Quer continuar? [S/N] ').strip().lower())
    
    cad +=1
    si += info['idade']
    if cont == 'n':
        break

print(f'- Foram cadastrada {cad} pessoas')
print(f'- A média de idade foi {si/cad}')
print('- As mulheres cadastradas foram',end=' ')
for p in pessoas:
    if p['sexo'] == 'f':
        print(p['nome'],end=' ')
print(f'- Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > si/cad:
        print(f'{f"Nome = {p['nome']}, Sexo = {p['sexo']}, idade = {p['idade']};":>35}')