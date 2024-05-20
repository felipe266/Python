from categoria import Categoria


def criar_arquivo(nome):
    try:
        arq = open(f'POO/financas/banco_de_dados/{nome}.txt', 'wt+')
        arq.close()
    except:
        print('\033[0;31mHouve em erro na criação do arquivo\033[m')
    else:
        print('\033[0;32mArquivo criado com sucesso\033[m')


def cadastrar(valor, categoria, observacao, arq=0):
        try:
            arquivo = open(f'POO/financas/banco_de_dados/{arq}.txt','at')
            arquivo.write(f'{observacao};{valor:.2f};{categoria.nome}\n')
        except:
            print('\033[0;31mErro em cadastrar\033[m')
        else:
            print('\033[0;32mCadastrado com sucesso\033[m')


def arqexiste(nome):
    try:
        arq = open(f'POO/financas/banco_de_dados/{nome}.txt','rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def mostra_banco(nome):
    try:
        arq = open(f'POO/financas/banco_de_dados/{nome}.txt','rt')
    except:
        print('\033[0;31mErro em exibir o arquivo\033[m')
    else:
        dados= []
        for a in arq:
            dado = a.replace('\n','').split(';')
            dados.append(dado[:])
        
        print('Descrição        Valor            Categoria')
        print('='*45)
        for info in dados:
            for v in info:
                print(f'{str(v):<17}',end='')
            print()
        arq.close()

def mostra_saldo(nome):
    try:
        arq = open(f'POO/financas/banco_de_dados/{nome}.txt','rt')
    except:
        print('\033[0;31mErro em exibir o arquivo\033[m')
    else:
        total = 0
        for a in arq:
            dado = a.replace('\n','').split(';')
            dado[1] = float(dado[1])
            if dado[2] == 'despesas':
                total -= dado[1]
            else:
                total += dado[1]
        print(f'saldo total é de {total:.2f} R$'.replace('.',','))