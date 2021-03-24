def logger(func):
    def wrapper(*args, **kwargs):
        resalt = func(*args, **kwargs)
        my_generait = (f'{ln}:{type(ln)}' for ln in args)
        my_generait_1 = (f'{lm_1}={lm_2}{type(lm_2)}' for lm_1, lm_2 in kwargs.items())
        print(
            f'Тип аргументов функции {func.__name__}:{",".join(map(str, my_generait))}{",".join(map(str, my_generait_1))}')
        print(*args)
        print(kwargs)
        return resalt

    return wrapper


@logger
def my_func(*args, **kwargs):
    pass


my_type = my_func(6, 'Иван', [1, 3, 'Вася'], long=26, higt=17)