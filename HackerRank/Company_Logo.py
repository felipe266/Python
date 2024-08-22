s = str(input('nome da compania: '))

letra = {}
for l in s:
    n = s.count(l)
    if n >= 1:
        letra[l] = n

order = sorted(letra.items(), key=lambda x: x[1], reverse = True)

maior = 0
for n in range(len(order)):
    if order[0][1] == order[n][1]:
        maior += 1

if maior >= 3:
    temp = []
    for l in order:
        if order[0][1] == l[1]:
            temp.append(l)
    order = sorted(temp)
    for n in range(0,3):
        print(order[n][0], order[n][1])
if maior == 2:
    two = sorted(order[:2])
    for n in range(0,2):
        print(two[n][0], two[n][1])
    del order[:2]
    temp = []
    for l in order:
        if order[0][1] == l[1]:
            temp.append(l)
    temp = sorted(temp)
    print(temp[0][0],temp[0][1])
if maior == 1:
    print(order[0][0], order[0][1])
    order.pop(0)
    temp = []
    for l in order:
        if order[0][1] == l[1]:
            temp.append(l)
    if len(temp) >= 2:
        temp = sorted(temp)
        for n in range(0,2):
            print(temp[n][0],temp[n][1])
    if len(temp) == 1:
        print(temp[0][0], temp[0][1])
        temp.clear()
        order.pop(0)
        for l in order:
            if order[0][1] == l[1]:
                temp.append(l)
        temp = sorted(temp)
        print(temp[0][0], temp[0][1])

#---------------------OUTRA FORMA------------------------------
from collections import Counter
a=Counter(input())
print(a)
q=[]
for i in range(len(a)):
    q.append(0)
for i in sorted(a.items()):
    for m in range(len(list(reversed(sorted(a.values()))))):
        if i[1] == list(reversed(sorted(a.values())))[m] and q[m]==0:
            q[m]=i[0]
            break
for i in range(3):
    print(q[i],list(reversed(sorted(a.values())))[i])