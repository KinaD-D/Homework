while True:

    x, action, y = float(input('x = ')), input('action = '), float(input('y = '))

    if action == '0':
        break

    if action == '+':
        print('%(x)s + %(y)s = %(hp)s' % {'x': x, 'y': y, 'hp': x + y})

    elif action == '-':
        print('%(x)s - %(y)s = %(hp)s' % {'x': x, 'y': y, 'hp': x - y})

    elif action == '*':
        print('%(x)s * %(y)s = %(hp)s' % {'x': x, 'y': y, 'hp': x * y})

    elif action == '/':
        if y != 0:
            print('%(x)s / %(y)s = %(hp)s' % {'x': x, 'y': y, 'hp': x / y})

        else:
            print("Деление на ноль!")