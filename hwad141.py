import datetime
from hwad14_decor import data


def logger_decor(foo):
    def new_foo(*args):
        time = datetime.datetime.now()
        foo_name = foo.__name__
        result = foo(args)
        with open('path.txt', 'w', encoding='utf-8') as file:
            file.write(f'{time}\n'
                       f'Имя функции: {foo_name}\n'
                       f'Аргументы: {args}\n'
                       f'Результат: {result}')

        return file

    return new_foo


@logger_decor
def people(doc_number):
    """
    Выводит фамилию и имя по заданному номеру документа
    """
    counter = 0
    for doc in data.documents:
        if doc_number[0] in doc.values():
            counter += 1
    if counter == 0:
        print('Такого документа не существует')
    elif counter == 1:
        for doc in data.documents:
            if doc["number"] == doc_number[0]:
                print(doc["name"])
                doc_name = doc["name"]

    return doc_name


if __name__ == '__main__':
    people(input('Введите номер документа: '))
