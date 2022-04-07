txt = input('Введите строку: ')  # ПитоН - этО хорошО /или/ ПиТоН - ЭтО УДоБнО

x, y = 0, 0

x = [x + 1 for i in range(len(txt)) if txt[i] in txt.lower()]
y = [y + 1 for i in range(len(txt)) if txt[i] in txt.upper()]

text = (txt.lower() if x > y else txt.upper())

print(text)  # питон - это хорошо /или/ ПИТОН - ЭТО УДОБНО

print('*********************************')

x = [txt[i].islower() for i in range(len(txt))]
y = [txt[i].isupper() for i in range(len(txt))]

text = (txt.lower() if x.count(True) > y.count(True) else txt.upper())

print(text)  # питон - это хорошо /или/ ПИТОН - ЭТО УДОБНО
