n_en = int(input(''))
english = input('').split()
english = set(map(int,english))
n_fra = int(input(''))
france = input('').split()
france = set(map(int,france))

sym_difference = english.symmetric_difference(france)

print(len(sym_difference))