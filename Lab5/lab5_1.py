t = int(input())


def f(x, a):
    return int(x/a) + (x % a)


for kit in range(t):
    l, r, a = map(int, input().split())

    m = []
    for i in range(l, r+1):
        m.append(f(i, a))
    print(max(m))
