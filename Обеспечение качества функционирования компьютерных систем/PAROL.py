z = 22
N = 0
while N < 3:
    x = int(input('Введите пароль: '))
    if x == z:
        print('Вы успешно авторизовались!')
        break
    else:
        print('Пароль неверный')
        N = N + 1
else:
    print('Попытки кончились, Жаль!')