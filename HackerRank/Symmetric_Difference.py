def symmetric(array1, array2):
    m_dif = array1.difference(array2)
    n_dif = array2.difference(array1)
    union = list(m_dif.union(n_dif))
    union.sort()
    
    for num in union:
        print(num)


len_m = int(input('tamanho de m: '))
m = list(map(int,input().split()))
len_n = int(input('tamanho de n: '))
n = list(map(int,input().split()))

symmetric(set(m), set(n))

#------------------OUTRA FORMA------------------

len_m = int(input('tamanho de m: '))
m = set(map(int,input().split()))
len_n = int(input('tamanho de n: '))
n = set(map(int,input().split()))

m_diff = m.difference(n)
n_diff = n.difference(m)
symmetric = sorted(m_diff.union(n_diff))

for num in symmetric:
    print(num)