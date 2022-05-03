# 1 1 2 3 5 8 13 21 34 55    89 144 233 377...
def fib():
    fib.seq.append(fib.seq[-1] + fib.seq[-2])
    fib.stop -= 1
    return fib() if fib.stop > 0 else fib.seq[n-1]

n = int(input('Введите номер элемента числовой последовательности Фибоначчи: '))
fib.seq = [1, 1]
fib.stop = n - 2

print(f'{n}-й элемент: {fib()}')

