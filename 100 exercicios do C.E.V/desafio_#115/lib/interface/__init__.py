import time

def linha(tam = 40):
    return ('='*tam)


def alinhamento(msg):
    print(linha())
    print(f'{msg}'.center(40))
    print(linha())


def erroint(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except (TypeError, ValueError):
            print('\033[0;31mERRO! digite um número inteiro válido\033[m')
        else:
            return n


def opcao(opcao = ()):
    while True: 
        alinhamento('MENU PRINCIPAL')
        c = 1
        for p in opcao:
            print(f'\033[0;32m{c}\033[m - \033[0;34m{p}\033[m')
            c += 1
        print(linha())
        op = erroint('Sua opção: ')
        time.sleep(1)
        if op == 3:
            alinhamento('Saindo do sistema')
            break
        if 0 >= op or op > len(opcao):
            print('\033[0;31mDigite uma opção válida\033[m') 
        else:
            alinhamento(f'Opção {op}')
        time.sleep(1)
    return op