n,m = input().split()
array = list(map(int,input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for ar in array:
    if ar in A:
        happiness += 1
    if ar in B:
        happiness -= 1

print(happiness)