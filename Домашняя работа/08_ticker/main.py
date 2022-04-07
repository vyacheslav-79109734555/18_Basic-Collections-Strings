txt_1 = list(input('Первая строка: '))
txt_2 = list(input('Вторая строка: '))
x = len(txt_1)
count = 0
for i_txt in range(0, x):
    txt = []
    for smb in range(0, x):
        txt += txt_1[(i_txt + smb) % x]
    if txt == txt_2:
        print('Первая строка получается из второй со сдвигом:', i_txt)
        count += 1
        break
if count == 0:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


