t = int(input())

for kit in range(t):
    s = input()
    c = input()
    indexes_c = []

    for char in range(len(s)):
        if s[char] == c:
            indexes_c.append(char)

    flag = False
    for i in range(len(indexes_c)):
        if indexes_c[i] % 2 == 0:
            flag = True
            break

    if flag:
        print('YES')
    else:
        print('NO')
