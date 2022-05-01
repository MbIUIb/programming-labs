# 1 1 2 3 5 8 13 21 34 55    89 144 233 377...
def fib(fibonachi: list, stop):
    fibonachi.append(fibonachi[-1] + fibonachi[-2])
    stop -= 1

    if stop > 0:
        return fib(fibonachi, stop)
    else:
        return fibonachi[n-1]


n = int(input('Введите номер элемента числовой последовательности Фибоначчи: '))
fibonachi = [1, 1]
stop = n - 2

print(f'{n}-й элемент: {fib(fibonachi, stop)}')
