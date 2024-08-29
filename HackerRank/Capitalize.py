def solve(s):
    le = ''
    sc = s.strip().replace('','-')
    se = sc.strip().split('-')
    for n in range(1, len(se)):
        if se[n-1].strip() == '':
            le += se[n].capitalize()
        else:
            le += se[n]

    print(le)
    #------------------------OUTRA FORMA------------------------
    print(' '.join([i.capitalize() for i in s.split(" ")]))

frase= input()
solve(frase)