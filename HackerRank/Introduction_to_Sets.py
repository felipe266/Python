def average(array):
    array = set(array)
    s = 0
    for e in array:
        s += e
    average = s/len(array)
    return average


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)