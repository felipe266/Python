#EXERCÍCIO 22: Crie um programa que leia o nome completo de uma pessoa e mostre: --O nome com todas as letras maiúsculas e minúsculas. --Quantas letras ao todo (sem considerar espaços). --Quantas letras tem o primeiro nome.
nome = str(input('qual seu nome? ').strip())
frases = nome.split()
sem_espaco = ''.join(frases)

print(f'o nome: {nome} \n em letra maiúsculas:{nome.upper()} \n em minúsculas: {nome.lower()} \n quantidade de letras: {len(sem_espaco)} \n quantidade de letras do 1º nome: {len(frases[0])}')

print('*~~'*20)

#EXERCÍCIO 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
while True:
    num = int(input('um número de 0 a 9999: ').strip())
    milhar = (num//1000)
    cetena = (num//100) - (milhar *10)
    dezena = (num//10) - (num//100)*10
    unid = num - (num//10)*10
    print(f'Milhar  {milhar}')
    print(f'Cetena  {cetena}')
    print(f'Dezena  {dezena}')
    print(f'Unidade {unid}')
    cont = str(input('consinuar[S/N]: '))
    if cont in 'nN':
        break