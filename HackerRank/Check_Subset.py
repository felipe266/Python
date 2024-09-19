T = int(input())
for _ in range(T):
    n_A = int(input())
    A = set(map(int,input().split()))
    n_B = int(input())
    B = set(map(int,input().split()))
    A.difference_update(B)
    if len(A) == 0:
        print(True)
    else:
        print(False)