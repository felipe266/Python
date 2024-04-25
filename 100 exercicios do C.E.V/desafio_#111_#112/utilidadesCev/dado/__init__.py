def leiaDinheiro(preco):
    while True:
        p = str(input(preco).replace(',','.').strip())
        if p.isalpha() or p == '':
            print(f'\033[0;31mO valor "{p}" não é um número válido\033[m')
        else:
            m = 0
            while True:
                if p[m].isalpha():
                    print(f'\033[0;31mO valor "{p}" não é um número válido\033[m')
                    p = str(input(preco).replace(',','.').strip())
                    m = 0
                else:
                    if m == len(p)-1:
                        break
                    m +=1

            break
    return float(p)