def print_formatted(number):
    '''bala = []
    for n in range(1, number+1):
        bala.append(n)
        bala.append(oct(n)[2:])
        bala.append(str(hex(n)[2:]).capitalize())
        bala.append(bin(n)[2:])

    b = 0
    for m in range(0,len(bala)):
        print(f'{bala[m]}'.rjust(3,' '),end=' ')
        b += 1
        if b == 4:
            print()
            b = 0'''
    #-------------------outra forma---------------------------
    tamanho=len(str(bin(number))[2:])
    for i in range(1,number+1):
        print(str(i).rjust(tamanho,' '),oct(i)[2:].rjust(tamanho,' '),hex(i)[2:].upper().rjust(tamanho,' '),bin(i)[2:].rjust(tamanho,' '))

n = int(input())
print_formatted(n)