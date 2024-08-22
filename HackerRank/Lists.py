n = int(input('número de comandos: '))

lista = ['insert', 'print', 'remove', 'append', 'sort', 'pop', 'reverse']

temp = []
print(temp)
for _ in range(n):
    name, *posi = input('função: ').split()
    while name not in lista:
        name = input('função: +1')
    numers = list(map(int, posi))
    if name in lista:
        if name == lista[0] and len(posi) == 2:
            temp.insert(numers[0],numers[1])
        if name == lista[1]:
            print(temp)
        if name == lista[2]:
            temp.remove(numers[0])
        if name == lista[3]:
            temp.append(numers[0])
        if name == lista[4]:
            temp.sort()
        if name == lista[5]:
            temp.pop(len(temp)-1)
        if name == lista[6]:
            temp.reverse()
    elif name not in lista:
        print('não está')