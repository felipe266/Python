def print_rangoli(size):
    alfabeto= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    escolhido = alfabeto[:size]
    c = ''
    for i in range(size-1, -1, -1):
        print((c).rjust((size*2)-2,'-')+escolhido[i]+(c[::-1]).ljust((size*2)-2,'-'))
        c += f'{escolhido[i]}-'
    for i in range(1, size):
        c = c.replace(f'{escolhido[i-1]}-','').replace(f'{escolhido[i]}-','')
        print((c).rjust((size*2)-2,'-')+escolhido[i]+(c[::-1]).ljust((size*2)-2,'-'))
n = int(input())
print_rangoli(n)