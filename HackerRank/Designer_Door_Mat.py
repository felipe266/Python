altura, largura = input().split()
frase = 'WELCOME'
c = '.|.'
for i in range(int(int(altura)/2)):
    print((c*i).rjust(int((int(largura)-len(c))/2),'-')+c+(c*i).ljust(int((int(largura)-len(c))/2),'-'))

print(('').rjust(int((int(largura)-len(frase))/2),'-')+frase+('').ljust(int((int(largura)-len(frase))/2),'-'))

for i in range(int(int(altura)/2)-1, -1, -1):
    print((c*i).rjust(int((int(largura)-len(c))/2),'-')+c+(c*i).ljust(int((int(largura)-len(c))/2),'-'))