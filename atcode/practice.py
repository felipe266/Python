'''a = int(input())
b, c = map(int, input().split())
s = input()
sum = a + b + c
print(sum, s)'''

'''a, b = map(int, input().split())
pro = a * b

if pro%2 == 0:
    print('Even')
elif pro%2 == 1:
    print('Odd')'''

'''squares = input()
print(squares.count('1'))'''

'''N = int(input())
X = list(map(int, input().split()))
op = 0
cond = True
while cond:
    cont = 0
    c = []
    for n in range(len(X)):
        if X[n]%2 == 1:
            cond = False
        else:
            c.append(X[n]/2)
            cont += 1
        if cont == len(X):
            X = c[:]
            op += 1

print(op)'''

'''A = int(input())
B = int(input())
C = int(input())
X = int(input())

ways = 0
for na in range(0,A+1):
    for nb in range(0,B+1):
        for nc in range(0,C+1):
            if (500*(na)) + (100*(nb)) + (50*(nc)) == X:
                ways += 1

print(ways)'''

'''N, A, B = map(int, input().split())

sum = 0
for n in range(1,N+1):
    sum_digits = 0
    for num in f'{n}':
        sum_digits += int(num)
    if A <= sum_digits <= B:
        sum += n
print(sum)'''

'''N = int(input())
a = list(map(int,input().split()))

a_alice = a_bob = 0
while True:
    if len(a)>0:
        a_alice += max(a)
        a.remove(max(a))
        if len(a)>0:
            a_bob += max(a)
            a.remove(max(a))
    else:
        break
print(a_alice-a_bob)'''

'''N = int(input())
X = []

for _ in range(N):
    d = int(input())
    if d not in X:
        X.append(d)
print(len(X))'''

'''N,Y = map(int,input().split())

for nx in range(N):
    for ny in range(N):
        for nz in range(N):
            if nx + ny + nz == N:
                if nx*10 + ny*5 + nz == Y/1000:
                    x = nx
                    y = ny
                    z = nz
                    print(x,y,z)
                    exit()
print(-1,-1,-1)'''
#2d6r7e4a2m2s
#1d1r1e1a1m
T = ('eraser','erase','dreamer','dream')
d = list('eraser')
print(d[-6:])
S  = str(input())
for l in T:
    if l in S:
        S = S.replace(l,'')

if len(S) == 0:
    print('YES')
else:
    print('NO')