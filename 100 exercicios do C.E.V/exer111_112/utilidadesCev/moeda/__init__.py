def moeda(ope):
    return (f'R${ope:.2f}'.replace('.',','))

def aumentar(n=0, taxa=0, formata = True):
    aumento = n*((taxa/100)+1)
    return aumento if formata is False else moeda(aumento)


def diminuir(n=0,taxa=0, formata = True):
    diminuir = n*(1-(taxa/100))
    return diminuir if formata is False else moeda(diminuir)


def dobro(n=0, formata = True):
    dobro = n*2
    return dobro if formata is False else moeda(dobro)


def metade(n=0, formata = True):
    metade = n/2
    return metade if formata is False else moeda(metade)


def resumo(n,a,d):
    print('='*30)
    print(f'Lista de operações'.center(30))
    print('='*30)

    frases = (f'Preço analisado: \t{moeda(n)}',
              f'aumento de {a}%: \t{aumentar(n,a)}',
              f'desconto de {d}%: \t{diminuir(n,d)}',
              f'Dobro do preço: \t{dobro(n)}',
              f'Metade do preço: \t{metade(n)}'
              )

    for f in frases:
        print(f)