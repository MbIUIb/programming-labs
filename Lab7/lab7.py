dictionary = {'walk': ['ходьба', 'шаг', 'идти', 'гулять'],
              'wake': ['просыпаться', 'будить', 'бодрствование'],
              'game': ['игра', 'игровой'],
              'process': ['процесс', 'обрабатывать'],
              'programmer': ['программист'],
              'proxy': ['доверенный', 'уполномоченный', 'доверенность', 'полномочие'],
              'move': ['двигаться', 'движение', 'двигать'],
              'view': ['взгляд', 'вид', 'мнение'],
              'virtual': ['виртуальный', 'действительный', 'фактический'],
              'virus': ['вирус', 'зараза', 'яд']}


def append_pair():
    key = input('Введите слово-ключ: ').lower()
    val = input('Введите перевод(если слов несколько вводите через пробел): ').lower().split()

    if key in dictionary:
        flag = input(f'"{key}" уже есть в словаре. Обновить значение слова "{key}"? (Y/N): ')
        if flag == 'Y' or 'y':
            dictionary[key] = val
            print(f'Значение "{key}" обновлено')
        else:
            print(f'Оставлено старое значение "{key}"')
    else:
        dictionary[key] = val
        print(f'Значение "{key}" добавлено')


def delete_pair():
    key = input('Введите слово-ключ: ').lower()

    del dictionary[key]


def change_pair():
    key = input('Введите старое слово-ключ: ').lower()
    new_key = input('Введите новое слово-ключ: ').lower()
    new_val = input('Введите перевод(если слов несколько вводите через пробел): ').lower().split()

    if key not in dictionary:
        flag = input(f'"{key}" нет в словаре. Добавить "{key}"? (Y/N): ')
        if flag == 'Y' or 'y':
            dictionary[key] = val
            print(f'Значение "{key}" добавлено')
        else:
            print(f'"{key}" не добавлено')
    else:
        del dictionary[key]
        dictionary[new_key] = new_val
        print(f'Значение "{key}" обновлено')


def check():
    key = input('Введите слово-ключ: ').lower()

    if key in dictionary:
        print(f'"{key}" есть в словаре')
    else:
        print(f'"{key}" отсутствует в словаре')


def output_short_n(n=5):
    if type(n) == int:
        for key in dictionary:
            if len(key) < n:
                print(f'{key} - {dictionary[key]}')
    else:
        for key in dictionary:
            print(f'{key} - {dictionary[key]}')


def clear_dict():
    dictionary.clear()


def reverse():
    reverse_dict = {}
    for key in dictionary:
        for val in dictionary[key]:
            reverse_dict.setdefault(val, [])
            reverse_dict[val].append(key)
    return reverse_dict


def sort_dict():
    sort_list = list(dictionary.keys())
    sort_list.sort()

    for key in sort_list:
        print(f'{key} - {dictionary[key]}')


while True:
    print('_____________________________________________\n'
          '1 - добавить пару\n'
          '2 - удалить пару\n'
          '3 - проверить, есть ли в базе\n'
          '4 - вывести англ. слова короче 5 символов\n'
          '5 - очистить словарь\n'
          '6 - отсортировать словарь\n'
          '7 - вывести весь словарь\n'
          '8 - изменить пару\n'
          '9 - поменять местами ключи и значения\n'
          '10 - прекратить выполнение программы\n'
          '_____________________________________________\n')

    n = int(input('Введите номер операции: '))
    if n == 1:
        append_pair()
    elif n == 2:
        delete_pair()
    elif n == 3:
        check()
    elif n == 4:
        output_short_n()
    elif n == 5:
        clear_dict()
    elif n == 6:
        sort_dict()
    elif n == 7:
        output_short_n('all')
    elif n == 8:
        change_pair()
    elif n == 9:
        dictionary = reverse()
    elif n == 10:
        break
    print('\n\n\n')
