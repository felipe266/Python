s_en = int(input(''))
english = input('').split()
english = set(map(int,english))
s_fra = int(input(''))
france = input('').split()
france = set(map(int, france))

union = france.union(english)

print(len(union))