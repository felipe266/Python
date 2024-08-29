import textwrap

def wrap(string, max_width):
    frase = ''
    for n in range(len(string)):
        frase += string[n]
        if n+1 % max_width == 0:
            frase += '\n'
    return frase

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)