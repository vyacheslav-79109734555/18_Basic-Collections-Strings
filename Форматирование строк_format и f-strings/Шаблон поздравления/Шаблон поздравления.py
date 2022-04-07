while True:
    gratis_template = input('Введите шаблон поздравления,'
                            'в шаблоне используйте конструкцию: {name}: ')  # С днем рождения {name} !!!
    if '{name}' in gratis_template:
        break
    print('Ошибка: отсутствует конструкция {name}.')

print('Введите список имен (заканчивается на end: ')
name_list = []
while True:
    name = input('имя: ')  # Петя , Вася , end
    if name != 'end':
        name_list.append(name)
    else:
        break
for i_name in name_list:
    print(gratis_template.format(name=i_name))


