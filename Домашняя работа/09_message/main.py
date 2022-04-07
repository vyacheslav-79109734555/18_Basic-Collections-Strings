txt = input('Сообщение: ')
t = []
txt_rev = []
for i in txt:
    if i.isalpha():
        t.append(i)
    else:
        i.isalpha()
        t = t[::-1]
        txt_rev.append(t)
        txt_rev.append(i)
        t = []

for j in txt_rev:
    txt_reverse = ''.join(j)
    print(txt_reverse, end='')


