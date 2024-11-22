from cmath import phase
cod = str(input().split())
num = []
x = y = no = n_op = 0
for n in range(len(cod)):
    if cod[n] in '+-':
        no += 1
    if cod[n].isnumeric():
        num.append(cod[n])
    if no==1 and cod[n] in '+-':
        num.append(cod[n])
for n in num:
    if n in '-+':
        nop += 1
    if nop == 0 and n not in '-+':
        x = 10*x + int(n)
    if nop == 1 and n not in '-+':
        y = 10*y + int(n)

print(x,y)
    
'''print(((num[0]**2)+(num[1]**2))**(1/2))
print(phase(complex(num[0],num[1])))'''