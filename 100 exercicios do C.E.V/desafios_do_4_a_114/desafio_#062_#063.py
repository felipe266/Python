#EXERCÍCIO 62: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
num = int(input('1º termo da P.A: ').strip())
r = int(input('razão P.A: ').strip())

pa = n = 1
while pa != num + (9)*r:
    pa = num + (n-1)*r
    n += 1
    print(f'{pa} ⇒',end=' ')
print('ESPERARANDO')

termo = pa2 = n = 1
while termo != 0:
    termo = int(input('quatos termos quer ver? '))
    if termo != 0:
        while pa2 != pa + (termo)*r:
            pa2 = pa + (n)*r
            n += 1
            print(f'{pa2} ⇒',end=' ')
        pa = pa2
        n = 1
        print('ESPERANDO')
print('FIM')

print('~='*20)

#EXERCÍCIO 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
n = int(input('quanto termos quer ver? '))

m = t3 = 0
t1 = 1
while m < n:
    t2 = t3 
    t3 = t1 + t2
    t1 = t2
    print(f'{t3} ⇒',end=' ')
    m+=1
print('FIM')