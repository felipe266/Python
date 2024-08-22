def count_substring(string, sub_string):
    conjunto = []
    f = ''
    for n in range(0, len(string)):
        conjunto.append(string[n:][:len(sub_string)])
    return conjunto.count(sub_string)

string = input('frase: ').strip()
sub_string = input('conjunto: ').strip()
    
count = count_substring(string, sub_string)
print(count)