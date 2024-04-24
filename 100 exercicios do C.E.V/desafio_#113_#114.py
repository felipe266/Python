#113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaint(msg):
    n = str(input(msg).strip())
    while True:
        if n.isnumeric() == False:
            print(f'\033[0;31mERRO! digite um número inteiro válido\033[m')
            n = input(msg)
        else:
            break
    return n

def leiaFloat(msg):
    while True:
        n = str(input(msg).strip())
        if n.isalpha() or n == '':
            print(f'\033[0;31mERRO! digite um número inteiro válido\033[m')
        else:
            m = 0
            while True:
                if n[m].isalpha():
                    print(f'\033[0;31mERRO! digite um número Real válido\033[m')
                    n = str(input(msg))
                    m = 0
                elif n[m] == ',':
                    print(f'\033[0;31mERRO! troco "," por "."\033[m')
                    n = str(input(msg))
                    m = 0
                else:
                    if m == len(n)-1:
                        break
                    m += 1

            break
    return n

'''i = leiaint('Digite um Inteiro: ')
r = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {i} e o real foi {r}')'''

print('~='*20)

#EXERCÌCIO 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import requests, time, webbrowser

url = 'http://www.pudim.com.br/'
try:
    site = requests.head(url,timeout=10)

except requests.exceptions.RequestException:
    print(f'\033[31mO site está inacessível no momento.\033[m')

else:
    print(f'\033[32mO site está acessível no momento.\033[m')
    time.sleep(1)
    webbrowser.open(url)