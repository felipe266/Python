from funcionarios import Funcionario
from criando_banco import criar_arquivo, arq_existe


def cadastrar():
    dados = []
    temp = []
    while True:
        if arq_existe():
            try:
                arquivo = open('controle_cotas_disco/banco/usuarios.txt', 'at')
                f = Funcionario(
                        str(input('Nome: ')),
                        int(input('Espaço(bytes): '))
                )
                arquivo.write(f'{f.nome};{f.espaco}\n')
            except:
                print('\033[0;31mErro em cadastrar\033[m')
            else:
                print('\033[0;32mCadastrado com sucesso\033[m')
        else:
            print('\033[0;31mArquivo não existe\033[m')
            criar_arquivo()
        cont = str(input('Deseja continuar?[S/N] ').strip())
        if cont in 'Nn':
            break