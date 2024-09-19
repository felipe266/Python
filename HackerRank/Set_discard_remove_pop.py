n = int(input())
s = set(map(int, input().split()))
func = ['pop', 'discard', 'remove']

for _ in range(n):
    comando = input('').split()
    if comando[0] == func[0]:
        s.pop()
    if comando[0] == func[1]:
        s.discard(int(comando[1]))
    if comando[0] == func[2]:
        s.remove(int(comando[1]))
    print(s)

sum = 0
for num in s:
    sum += num

print(s)