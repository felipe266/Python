#EXERCÌCIO 20: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import randint
from time import sleep

student = ['rivaldo', 'raimunda', 'felipe','maria']
print(f'dos estudante {student} a ordeme sorteada foi')
sleep(1)
for s in range(0,len(student)):
    chosen = randint(0,len(student)-1)
    print(student[chosen])
    student.remove(student[chosen])
    sleep(1)

print('*~~'*20)

#EXERCÍCIO 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.