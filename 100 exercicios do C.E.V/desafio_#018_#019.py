#EXERCÍCIO 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angle = str(input('Digite um ângulo em graus(º): ').strip())
angle = float(angle.replace(',', '.'))

radi = math.radians(angle)
sen = math.sin(radi)
cos = math.cos(radi)
tan = math.tan(radi)

print(f'o ângulo {angle}º tem seno de {sen:.3f} cosseno {cos:.3f} e tangente {tan:.3f}')

print('*~~'*20)

#EXERCÍCIO 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

student = []
c = 1
while True:
    student.append(input(f'qual o {c}º: '))
    if c == 4:
        break
    c += 1
chosen = random.randint(0,3)

print(f'dos alunos {student} o sorteado foi {student[chosen]}')