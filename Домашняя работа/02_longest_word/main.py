txt = input('Введите строку: ').split()

max_word = [i for i in txt if len(i) == max([len(j_txt) for j_txt in txt])]
print('Самое длинное слово: ', ''.join(max_word))

length = max([len(i) for i in txt])
print('Длина этого слова: ', length)
