import datetime

def logger_decor(foo):


    def new_foo(*args, **kwargs):

        time = datetime.datetime.now()
        foo_name = foo.__name__
        result = foo(args, kwargs)
        with open('path.txt', 'w', encoding = 'utf-8') as file:
            file.write(f'{time}\n'
                       f'Имя функции: {foo_name}\n'
                       f'Аргументы: {args}\n'
                       f'{kwargs}\n'
                       f'Результат: {result}')

        return file

    return new_foo

@logger_decor
def func(a, b):
    s = [a, b]
    return s
