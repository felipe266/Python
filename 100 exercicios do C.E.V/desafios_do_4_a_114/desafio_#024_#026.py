#EXERCÍCIO 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
#EXERCÍCIO 25: IGUAL DO 24
cidade = str(input('O nome da sua cidade? ').strip().lower())

if cidade.split()[0] == 'santos':
    print(f'sua cidade {cidade} começa com SANTOS')
else:
    print(f'sua cidade {cidade} nao começa com SANTOS')

print('*~~'*20)

#EXERCÍCIO 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('escreve algo aí: ').strip().lower())

print(f'A letra A apareceu: {frase.count('a')} vez \napareceu pela 1º vez na posição: {frase.find('a') + 1} \napareceu pela ultima vez: {frase.rfind('a') + 1}')

#outra forma de ver a ulta posição
'''for a in range(0,len(frase)):
    if frase[a] == 'a':
        ultimo = a
        
print(f'A apareceu pela ultima vez na posição: {ultimo + 1}')'''