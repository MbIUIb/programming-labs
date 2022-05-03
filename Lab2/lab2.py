if (number := int(input('Введите число: '))) > 1:
    count = 2

    for divider in range(2, int(number**0.5)+1):
        if number % divider == 0:
            count += 1

        if count > 2:
            break

    if count == 2:
        print(f'Число {number} является простым')
    else:
        print(f'Число {number} не является простым')
else:
    print(f'Число {number} не является простым')
