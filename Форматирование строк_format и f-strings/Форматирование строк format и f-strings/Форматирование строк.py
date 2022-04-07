path = 'C:/{user}/docs/folder/{new_file}.txt'.format(
    user=input('Введите имя пользователя: '),
    new_file=input('Введите имя файла: '))

print(path)

'''
в данном случае в стоке:
// 'C:/{0}/docs/folder/{1}.txt' //
{0} = Введите имя пользователя:
{1} = Введите имя файла: 
'''
# предпочтительный формат в написании кода:
path_2 = 'C:/{0}/docs/folder/{1}.txt'.format(
    input('Введите имя пользователя: '),
    input('Введите имя файла: '))

print(path)

'''
метод f-strings 
'''

a = input('Введите имя пользователя: ')
b = input('Введите имя файла: ')

path_3 = f'C:/{a}/docs/folder/{b}.txt'

print(path_3)

a = input('Введите имя пользователя: ')
b =  input('Введите имя файла: ')

path_4 = 'C:/{0}/docs/folder/{1}.txt'.format(a, b)

print(path_4)