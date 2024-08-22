def mutate_string(string, position, character):
    frase = ''
    for n in range(len(string)):
        if n == position-1:
            frase += character
        else:
            frase += string[n]
            
    return frase

if __name__ == '__main__':
    s = input('frase: ')
    i, c = input('mudança: ').split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)