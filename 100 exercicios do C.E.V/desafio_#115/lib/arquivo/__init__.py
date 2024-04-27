def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        arquivo = open(nome,'wt+')
        arquivo.close()
    except:
        print('\033[0;31mHouve uma erro\033[m')
    else:
        print(f'\033[0;32marquivo {nome} criado com sucesso\033[m')

def lerarquivo(arq):
    try:
        ar = open(arq,'rt')
    except:
        print('\033[0;31mNão tem cadastros\033[m'.upper())
    else:
        for n in ar:
            dado = n.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30} {dado[1]:>3}Anos')

def cadastrar(nome = 'Nome: ', idade = 'idade: ', arq = 0):
    try:
        cadnome = str(input(nome))
        cadidade = str(input(idade))
        arquivo = open(arq, 'at')
        arquivo.write(f'{cadnome};{cadidade}\n')
    except:
        print('\033[0;31mNão tem cadastros\033[m'.upper())
    else:
        print(f'\033[0;32mCadastrado com sucesso\033[m')