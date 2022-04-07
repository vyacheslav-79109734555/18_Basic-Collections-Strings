while True:
    txt = list(input('Придумайте пароль: '))
    f1 = f2 = f3 = False
    for i in txt:
        if i.isupper():
            f1 = True
        elif i.islower():
            f2 = True
        elif i.isdigit:
            f3 = True

    if f1 and f2 and f3 >= 3 and len(txt) > 8:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
