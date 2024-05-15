def criar_arquivo(nome):
    try:
        arq = open(f'POO/financas/banco_de_dados/{nome}', 'wt+')
        arq.close()
    except:
        print('\033[0;31mHouve em erro na criação do arquivo\033[m')
    else:
        print('\033[0;32mArquivo criado com sucesso\033[m')