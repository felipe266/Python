n = int(input('number of parameters: '))
student_marks = {}
for _ in range(n):
    name, *line = input('student: ').split()
    print(line)
    scores = list(map(int, line))
    print(scores)
    #MAP() aplica uma fução em todos os intens de uma lista, ou seja aplica a função float na lista line
    student_marks[name] = scores

query_name = input('query name: ')

notas = student_marks[query_name]

s = 0
for n in notas:
    s += n/3

print(f'{s:.2f}')