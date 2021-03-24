def val_checker(func):
    def wrapper(*args):
        try:
            if args[0] > 0:
                resalt = func(*args)
                return resalt
            else:
                raise ValueError
        except ValueError:
            return f'{ValueError}: wrong val {x}'

    return wrapper


@val_checker
def calc_cube(x):
    return x ** 3


x = int(input('Введите число :'))
a = calc_cube(x)
print(a)
