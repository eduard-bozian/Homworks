def add_everything_up(a, b):
    try:
        if a != b:
         return str(a) + str(b)
    except TypeError:
        print(f'Не верный тип данных!')
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
