def merge_the_tools(string, k):
    frase = []
    for n in range(len(string)):
        if n == 0:
            frase.append(string[n:][:k])
        else:
            ...
    print(frase)

string, k = input(), int(input())
merge_the_tools(string, k)