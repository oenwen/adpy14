import datetime
from hwad14_decor import data


def parametrized_logger_decor(path):
    def logger_decor(foo):
        def new_foo(*args, **kwargs):
            time = datetime.datetime.now()
            foo_name = foo.__name__
            result = foo(args, kwargs)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(f'{time}\n'
                           f'Имя функции: {foo_name}\n'
                           f'Аргументы: {args}\n'
                           f'{kwargs}\n'
                           f'Результат: {result}')

            return file

        return new_foo

    return logger_decor


@parametrized_logger_decor('path1.txt')
def add(*args, **kwargs):
    """
    добавляет новый документ в базу
    """

    if new_shelf not in data.directories:
        print('Такой полки не существует, будет создана новая полка')
        data.directories[new_shelf] = []
    new_doc = {"type": new_type, "number": new_number, "name": new_person}
    data.documents.append(new_doc)
    data.directories[new_shelf].append(new_number)

    return new_doc


if __name__ == '__main__':
    new_number = input('Введите номер нового документа ')
    new_type = input('Введите тип нового документа ')
    new_person = input('Введите имя и фамилию ')
    new_shelf = input('Введите номер полки, на которую нужно добавить новый документ ')
    add(new_number, new_type, new_person, new_shelf)
