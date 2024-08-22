coisa = str(input('coisa: '))

al = alp = di = lo = up = 0
for l in coisa:
    if l.isalnum():
        al += 1
    if l.isalpha():
        alp += 1
    if l.isdigit():
        di += 1
    if l.islower():
        lo += 1
    if l.isupper():
        up += 1

if al >= 1:
    print('True')
else:
    print('False')
if alp >= 1:
    print('True')
else:
    print('False')
if di >= 1:
    print('True')
else:
    print('False')
if lo >= 1:
    print('True')
else:
    print('False')
if up >= 1:
    print('True')
else:
    print('False')