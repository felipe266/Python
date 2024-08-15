superset  = input('superset: ').split()
score = set(list(map(int,superset)))
numbers_subset = int(input('numbers of subset: '))

condition=[]
for _ in range(numbers_subset):
    sets = input('sets: ').split()
    score1 = list(set(map(int, sets)))
    inter = score.intersection(score1)
    if len(inter) < len(score1):
        condition.append('False')
    elif len(inter) == len(score1):
        condition.append('True')

if condition.count('False') > 0:
    print('False')
else:
    print('True')