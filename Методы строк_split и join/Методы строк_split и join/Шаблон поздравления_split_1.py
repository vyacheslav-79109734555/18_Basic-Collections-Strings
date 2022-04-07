while True:  # С днем рождения {name} !!! Тебе уже {age} лет !
    gratis_template = input('Введите шаблон поздравления,'
                            'в шаблоне используйте конструкцию: {name} и {age}: ')
    if '{name}' in gratis_template and '{age}' in gratis_template:
        break
    print('Ошибка: отсутствует конструкция {name} или {age}.')

name_list = input('Список людей через запятую: ').split(', ')  # Петя Петров, Иван Иванов
age_str = input('Возраст людей через пробел: ')  # 20 30
age_list = [int(i_num) for i_num in age_str.split()]

for i_man in range(len(name_list)):
    print(gratis_template.format(name=name_list[i_man], age=age_list[i_man]))

people_ages = [' '.join([name_list[i_arr], str(age_list[i_arr])]) for i_arr in range(len(name_list))]

print(people_ages)

people_ages_str = ', '.join(people_ages)

print('\nИменинники:', people_ages_str)
