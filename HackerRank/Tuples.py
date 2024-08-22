n = int(input()) 
while True:
    nums = input('').split()
    lista = tuple(map(int, nums))

    if len(lista) == n:
        break
    else:
        print('digite a quantidade {n} de caraqueteres')
print(lista)
print(hash(lista))
#FAZER NO PYPY3