n_en = int(input(''))
english = input('').split()
english = set(map(int,english))
n_fra = int(input(''))
france = input('').split()
france = set(map(int, france))

intersection = english.intersection(france)
print(len(intersection))