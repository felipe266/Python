from criando_banco import arq_existe2, criar_arquivo2


def gerar_templete():
    if arq_existe2():
        try:
            frase = 'ACME Inc.             Uso do espaço em disco pelos usuários         \n'
            arq = open('controle_cotas_disco/banco/relatorio.txt','at+')
            arq.write(frase)
            arq.write('-'*len(frase))
            arq.write('\nNr.  Usuário        Espaço utilizado        %  do uso\n\n')
            arq.close()
        except:
            print('\033[0;31mErroiufefd ao cadastrar\033[m')
        else:
            print('\033[0;32mCadastrado com sucesso\033[m')
    else:
        criar_arquivo2()


def gerar_usuarios():
    try:
        arq = open('controle_cotas_disco/banco/usuarios.txt', 'rt')
    except NameError as e:
        print('\033[0;31mErro ao ler o arquivo\033[m\n',e)
    else:
        try:
            dados = []
            total = 0
            for a in arq:
                dado = a.replace('\n','').split(';')
                if len(dado[0]) < 10:
                    t = 10 - len(dado[0])
                    dado[0] = dado[0] + '.'*t
                dado[1] = str(float(dado[1]) * float(9.53674*10**(-7))).split('.')
                total += float(dado[1])
                dado[1] = dado[1][0] +','+ dado[1][1][:2]
                print(dado[0], f'{dado[1]:>10}',f'{'MB':<5}')
            print(total)
        except NameError as e:
            print(e)