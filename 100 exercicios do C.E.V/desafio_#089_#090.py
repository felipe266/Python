#EXERCÍCIO 89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
pessoas = []
temp = []
c = 0
while True:
    temp.append(str(input(f'Nome: ').strip()))
    temp.append(float(input(f'Nota1: ').strip().replace(',','.')))
    temp.append(float(input(f'Nota2: ').strip().replace(',','.')))
    pessoas.append(temp[:])
    temp.clear()
    cont = str(input('quer continuar? [S/N]').strip())
    if cont in 'nN':
        break
print('No. Nome',f'{"Média":>20}')
for aluno in pessoas:
    print(c,end=f'{'':>3}')
    print(aluno[0],end=f'{'':<15}')
    print(f'{((aluno[1] + aluno[2])/2):.1f}')
    c += 1

while True:
    no = int(input('Mostrar nota de qual aluno? (999para): ').strip())
    if no == 999:
        break
    if no > len(pessoas)-1:
        print('não existe essa pessoa')
    else:
        print(f'A nota de {pessoas[no][0]} é de [{pessoas[no][1]} ,{pessoas[no][2]}]')