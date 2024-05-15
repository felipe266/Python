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
            arquivo.write(f'{observacao};{valor};{categoria.nome}\n')
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