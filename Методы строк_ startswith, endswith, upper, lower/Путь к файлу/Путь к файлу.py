user_name = input('Введите пользователя: ')
file_name = input('Введите имя файла: ')

path = 'C:/{user}/docs/folder/{new_file}'.format(user=user_name, new_file=file_name)

if not path.endswith('.txt'):
    print('Ошибка: неверное расширение файла')
elif not path.startswith('C:/'):
    print('Ошибка: неверное указан диск')
else:
    print('Путь к файлу:', path)
