from criando_banco import arq_existe2, criar_arquivo2


def gerar_templete():
    if arq_existe2():
        try:
            frase = 'ACME Inc.             Uso do espaço em disco pelos usuários         \n'
            arq = open('controle_cotas_disco/banco/relatorio.txt','at+')
            arq.write(frase)
            arq.write('-'*len(frase))
            arq.write('\nNr.Usuário        Espaço utilizado        %  do uso\n\n')
            arq.close()
        except:
            print('\033[0;31mErroiufefd ao cadastrar\033[m')
    else:
        criar_arquivo2()


def gerar_usuarios():
    try:
        arq = open('controle_cotas_disco/banco/usuarios.txt', 'rt')
        arquivo = open('controle_cotas_disco/banco/relatorio.txt', 'at')
    except NameError as e:
        print('\033[0;31mErro ao ler o arquivo\033[m\n',e)
    else:
        try:
            dados = []
            total = 0
            #cadastrando em DADOS
            for n,a in enumerate(arq):
                dado = a.replace('\n','').split(';')
                dados.append(dado)
                dados[n][1] = f'{float(dados[n][1]) * float(9.53674*10**(-7)):.2f}'
            total += float(dados[n][1])
            arq.close()
            #cadastrando no .txt
            for n, d in enumerate(dados):
                if len(d[0]) < 10:
                    t = 10 - len(d[0])
                    d[0] = d[0] + ' '*t
                print(
                porcetagem = f'{((float(d[1])/total)*100):.2f}'
                #print(porcetagem)
                #ordem de espaço
                post = ant = 0
                '''for d in range(len(dados)):
                    for nu in range(len(dados)):
                        if dados[nu][1] <= dados[d][1]:
                            post = dados[nu]
                            ant = dados[d]
                            dados[d] = post
                            dados[nu] = ant'''
            for n, d in enumerate(dados):
                #arquivo.write(f'{d}\n')
                #tamanho do armazenamento formatado em str
                arquivo.write(f'{n+1} {d[0]} {d[1]:>15} {'MB':<5} {porcetagem:>13} {'%':<5}\n'.replace('.',','))
            arquivo.write(f'\nEspaço total ocupado: {total:.2f} MB\n'.replace('.',','))
            arquivo.write(f'Espaço medio ocupado: {(total/(n+1)):.2f} MB\n'.replace('.',','))
            arquivo.close()
        except NameError as e:
            print(f'\033[0;31m{e}\033[m')
        else:
            print('\033[0;32mCadastrado com sucesso\033[m')