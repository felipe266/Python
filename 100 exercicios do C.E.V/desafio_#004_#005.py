#EXERCÍCIO 4
algo = input('Digite algo: ')
print(f'qual o formato? {type(algo)}')
print(f'é alfanumerico? {algo.isalnum()}')
print(f'é alfabético? {algo.isalpha()}')
print(f'é um número? {algo.isnumeric()}')
print(f'só tem espaço? {algo.isspace()}')
print(f'está maiúsculo? {algo.isupper()}')
print(f'está minúsculo? {algo.islower()}')
print(f'a 1º letra é maiúscula? {algo.istitle()}')

print('*~~'*20)

#EXERCÍCIO 5
num = int(input('DIgite um número? ').strip())

antecessor = (num - 1)
sucessor = (num + 1)

print(f'O número {num} tem como o antecessor {antecessor} e sucessor {sucessor}')