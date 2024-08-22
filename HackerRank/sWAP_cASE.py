def swap_case(s):
    f = ''
    for n in range(len(s)):
        if s[n].isupper():
           f += s[n].lower()
        else:
            f += s[n].upper()
    return f

frase = str(input('frase: '))
result = swap_case(frase)
print(result)