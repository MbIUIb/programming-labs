for kit in range(int(input())):
    s, c = input(), input()
    indexes_c = [idx for idx, char in enumerate(s) if char == c]

    if any(map(lambda x: not x % 2, indexes_c)):
        print('YES')
    else:
        print('NO')
