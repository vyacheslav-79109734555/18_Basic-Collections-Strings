q = 0
ip = []
while q != 4:
    n = input(f'Введите {len(ip) + 1}-е число IP-адреса компьютера: ')
    if not n.isdigit() or int(n) < 0 or int(n) > 255:  # Обеспечьте контроль ввода.
        print('Ошибка ввода')
    else:
        ip.append(n)
        q += 1

print('.'.join(ip))

ip_address = '{}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3])

print('*', ip_address)
