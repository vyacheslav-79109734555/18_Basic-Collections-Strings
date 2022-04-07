text = input('Введите текст: ')  # У     нас      пошёл      снег    !
words_list = text.split()

print(words_list)

print(*words_list)

print(' '.join(words_list[:2]), ' '.join(words_list[3:]))

new_text = ' * '.join(words_list)

print(new_text)
