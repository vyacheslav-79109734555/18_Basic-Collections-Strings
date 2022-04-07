txt = input('Введите строку: ')
t = txt[0]
count = 1
res = ''
for i in range(len(txt) - 1):
    c = txt[i + 1]
    if t == c:
        count += 1
    else:
        res += t + str(count)
        count = 1
        t = c
res += t + str(count)
print(res)


