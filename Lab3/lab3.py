string = input('Введите строку: ') #'qwe*qwer*qw*qw e rty*'
list_str = string.split('*')

# находим максимальную подстроку
max_substr = ''
for substr in list_str:
    if len(substr) > len(max_substr):
        max_substr = substr


# забороподобная строка
fence = ''
count = 0
for i in range(len(max_substr)):
    if max_substr[i] != ' ':
        if count % 2 == 0:
            fence += max_substr[i].upper()
        else:
            fence += max_substr[i].lower()
        count += 1
    else:
        fence += ' '


print(f'строка: {fence}     длина строки: {len(max_substr)}')
