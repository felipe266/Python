def moeda(m,frase):
    print(f'{frase} R${m:.2f}'.replace('.',','))


def aumentar(n=0, taxa=0, format=False):
    aumento = n*((taxa/100)+1)
    if format is True:
        moeda(aumento,f'Com aumento de {taxa}%, temos ')
    else:
        print(f'Com aumento de {taxa}%, temos {aumento}')


def diminuir(n=0,taxa=0, format=False):
    diminuir = n*(1-(taxa/100))
    if format is True:
        moeda(diminuir,f'Com desconto de {taxa}%, temos')
    else:
        print(f'Com desconto de {taxa}%, temos {diminuir}')

def dobro(n=0,format=False):
    if format is True:
        moeda(n*2, f'o dobro de R${n:.2f}')
    else:
        print(f'o dobro de R${n:.2f} é {n*2}')

def metade(n=0, format=False):
    if format is True:
        moeda(n/2, f'a metade de R${n:.2f}')
    else:
        print(f'a metade de R${n:.2f} é {(n/2):.2f}')


def resumo(n,a,d):
    aumentar(n,a,format=True)
    diminuir(n,d,format=True)
    dobro(n,format=True)
    metade(n,format=True)
    