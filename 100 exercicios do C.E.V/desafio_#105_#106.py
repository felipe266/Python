#EXERCÍCIO 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:- Quantidade de notas- A maior nota- A menor nota- A média da turma- A situação (opcional)
def notas(*notas, sit = False):
    media = 0
    for n in range(0,len(notas)):
        media += (notas[n]/len(notas))
        if n == 0:
            maior = notas[n]
            menor = notas[n]
        else:
            if notas[n] >= maior:
                maior = notas[n]
            elif notas[n] <= menor:
                menor = notas[n]
    info = {'total': len(notas), 'maior': maior, 'menor': menor, 'media': media}
    if sit == True:
        if media < 6:
            info['situação'] = 'ruim'
        else:
            info['situação'] = 'boa'
    return info


resp = notas(5.5, 2.5, 10, 6.5)
print(resp)

print('~='*15)

#EXERCÍCIO 106: Make a mini-system that utilizes Python Interactive Help. The user is going to type the command and the manual will show up. When the user types the word 'FIM' ('END'), the program will close. Important: Use colors.
c = ('\033[m',         #0-sem cor
     '\033[0;30;41m',  #1-vermelho
     '\033[0;30;42m',  #2-verde
     '\033[0;30;43m',  #3-amarelo
     '\033[0;30;44m',  #4-azul
     '\033[0;30;45m',  #5-roxo
     '\033[0;30m'      #6-branco
     )
def frase(msg,cor=0):
    tam = len(msg)+4
    print(f'{c[cor]} ','-'*tam,f'{c[0]} ')
    print(f'{c[cor]}  {msg}     {c[0]}')
    print(f'{c[cor]} ','-'*tam,f'{c[0]} ')


def ajuda(frase):
    while True:
        ajuda = input(frase).lower()
        if ajuda == 'fim':
            break
        if ajuda in '':
            print('Digite algo')
        else:
            print(f'{c[4]}')
            help(ajuda)
            print(f'{c[0]}')

frase('Sistema de ajuda em python',2)
ajuda('Função ou biblioteca > ')
frase('Programa encerrado',1)