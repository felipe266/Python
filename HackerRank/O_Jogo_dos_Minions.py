def minion_game(string):
    vogais = 'aeiou'
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    v = ''
    c = ''
    for s in string:
        if s in vogais:
            v += s
        if s in consoantes:
            c += s
    k = len(v)
    st = len(c)


s = input()
minion_game(s)