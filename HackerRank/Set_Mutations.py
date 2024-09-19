n_A = int(input(''))
A = set(map(int, input('').split()))
N = int(input(''))
operations = ('intersection_update', 'update', 'symmetric_difference_update', 'difference_update')
for _ in range(N):
    operation = input('').split()
    num = set(map(int, input().split()))
    if operation[0] in operations:
        if operation[0] == operations[0]:
            A.intersection_update(num)
        if operation[0] == operations[1]:
            A.update(num)
        if operation[0] == operations[2]:
            A.symmetric_difference_update(num)
        if operation[0] == operations[3]:
            A.difference_update(num)
print(sum(A))