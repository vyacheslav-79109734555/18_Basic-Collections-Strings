def determine(t):
    if t == 1: return i + ' - не целое число'
    if t == 2: return i + ' - превышает 255'
    if t == 3: return 'Адрес - это четыре числа, разделенные точками'
    if t == 4: return 'IP-адрес корректен'


txt = input('Введите IP: ').split('.')
k = len(txt)
for i in txt:
    if k != 4:
        tmp = 3
        break
    if not i.isdigit():
        tmp = 1
        break
    if int(i) > 255:
        tmp = 2
        break
    tmp = 4
print(determine(tmp))


