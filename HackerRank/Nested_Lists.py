def lowest(st):
    itens = st
    for n in range(len(itens)):
        if n == 0:
            num = itens[n][1]
        else:
            if num > itens[n][1]:
                num = itens[n][1]
    return num
       

q = int(input('Number of parameters: ').strip())

students = []
temp = []
for _ in range(q): 
    name = input('name: ')
    score = float(input('score: '))
    temp.append(name)
    temp.append(score)
    students.append(temp[:])
    temp.clear()

min = lowest(students)

new_students = []
for i in students:
    if i[1] != min:
        new_students.append(i[:])

min = lowest(new_students)

second_lowest = []
for s in new_students:
    if s[1] == min:
        second_lowest.append(s[0])

order = sorted(second_lowest)
for o in order:
    print(o)

#------------------------OUTRA FORMA------------------------
studentlist = []

for _ in range(int(input('quantity: '))):
    name = input('name: ')
    score = float(input('score: '))
    studentlist.append([name,score])

secondmin = sorted(list(set([x[1] for x in studentlist])))
print(secondmin)
secondmin = secondmin[1]
finallist = sorted([x[0] for x in studentlist if x[1] == secondmin])
for a in finallist:
    print(a)

#SET() são coleções de intens que não podem conter elementos duplicados, parcialmete imutavel
meu_set = {1, 2, 3, 4, 1}
meu_set_2 = set([1, 2, 8, 9, 10])

# União
print("União")
print(meu_set | meu_set_2)
print(meu_set.union(meu_set_2))

# Interseção
print("Interseção")
print(meu_set & meu_set_2)
print(meu_set.intersection(meu_set_2))

# Diferença
print("Diferença")
print(meu_set - meu_set_2)
print(meu_set.difference(meu_set_2))

# Diferença Simétrica
print("Diferença Simétrica")
print(meu_set ^ meu_set_2)
print(meu_set.symmetric_difference(meu_set_2))