def split_and_join(line):
    # line = line.replace(' ', '-')
    line = line.split()
    line = '-'.join(line)
    return line


line = input("frase: ")
result = split_and_join(line)
print(result)