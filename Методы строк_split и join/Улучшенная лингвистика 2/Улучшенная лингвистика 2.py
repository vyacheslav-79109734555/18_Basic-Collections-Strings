words = [input(f'Введите {i+1} слово: ') for i in range(3)]
text = input('Введите текст для поиска: ')
for word in words:
    print(f'Слово {word} встречается в тексте {text.count(word)} раз')
