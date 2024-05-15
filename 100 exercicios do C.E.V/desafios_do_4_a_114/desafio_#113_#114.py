#113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''def leiaint(msg):
    n = str(input(msg).strip())
    while True:
        if n.isnumeric() == False:
            print('\033[0;31mERRO! digite um número inteiro válido\033[m')
            n = input(msg)
        else:
            break
    return n

def leiaFloat(msg):
    while True:
        n = str(input(msg).strip())
        if n.isalpha() or n == '':
            print('\033[0;31mERRO! digite um número inteiro válido\033[m')
        else:
            m = 0
            while True:
                if n[m].isalpha():
                    print('\033[0;31mERRO! digite um número Real válido\033[m')
                    n = str(input(msg))
                    m = 0
                elif n[m] == ',':
                    print('\033[0;31mERRO! troco "," por "."\033[m')
                    n = str(input(msg))
                    m = 0
                else:
                    if m == len(n)-1:
                        break
                    m += 1

            break
    return n

i = leiaint('Digite um Inteiro: ')
r = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {i} e o real foi {r}')'''

print('-='*12)

#FAZENDO COM TRY E except:
def erroint(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except (TypeError, ValueError):
            print('\033[0;31mERRO! digite um número inteiro válido\033[m')
        else:
            return n


def errifloat(msg):
    while True:
        try:
            f = float(input(msg).strip().replace(',','.'))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! digite um número Real válido\033[m')
        else:
            return f


n = erroint('Digite um intério: ')
f = errifloat('Digite um Real: ')
print(f'O número intéro digitado foi {n} e o Real foi {f}')

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