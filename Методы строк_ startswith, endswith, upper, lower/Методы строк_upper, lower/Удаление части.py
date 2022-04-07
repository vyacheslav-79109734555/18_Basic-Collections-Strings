word = [input(f'Введите {i_num + 1} слово: ').lower() for i_num in range(3)]  # он она оно

# вводим: он Он Она ОнО, а записывается: // lower() // в нижнем реестре // он он она оно

text = input('Введите текст: ').lower().split()

print('\nПодсчет слов в тексте')
for index in range(3):
    print(word[index], ':', text.count(word[index]))

word = [input(f'Введите {i_num + 1} слово: ').upper() for i_num in range(3)]  # он она оно

# вводим: он Он Она ОнО, а записывается: // upper() // в ВЕРЖНЕМ реестре // ОН ОН ОНА ОНО

text = input('Введите текст: ').upper().split()

print('\nПодсчет слов в тексте')
for index in range(3):
    print(word[index], ':', text.count(word[index]))
