def criar_arquivo():
    try:
        arq = open('controle_cotas_disco/banco/usuarios.txt', 'wt+')
        arq.close()
    except:
        print('\033[0;31mHouve um erro ao criar o arquivo\033[m')
    else:
        print('\033[0;32mArquivo criado com sucesso\033[m')


def criar_arquivo2():
    try:
        arq = open('controle_cotas_disco/banco/relatorio.txt', 'wt+')
        arq.close()
    except:
        print('\033[0;31mHouve um erro ao criar o arquivo\033[m')
    else:
        print('\033[0;32mArquivo criado com sucesso\033[m')


def arq_existe():
    try:
        arq = open('controle_cotas_disco/banco/usuarios.txt', 'rt+')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
def arq_existe2():
    try:
        arq = open('controle_cotas_disco/banco/relatorio.txt', 'rt+')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True