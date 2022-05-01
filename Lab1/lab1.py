print('##################################')
# прямая
line_x1 = float(input('Введите x первой точки ПРЯМОЙ: '))
line_y1 = float(input('Введите y первой точки ПРЯМОЙ: '))
line_x2 = float(input('Введите x второй точки ПРЯМОЙ: '))
line_y2 = float(input('Введите y второй точки ПРЯМОЙ: '))

if line_x1 != line_x2:
    k = (line_y1 - line_y2) / (line_x1 - line_x2)
else:
    k = 'undef'
b = line_y1 - k * line_x1

print('**********************************')
# прямоугольник
rectangle_x1 = float(input('Введите x левой нижней точки ПРЯМОУГОЛЬНИКА: '))
rectangle_y1 = float(input('Введите y левой нижней точки ПРЯМОУГОЛЬНИКА: '))
rectangle_x2 = float(input('Введите x правой верхней точки ПРЯМОУГОЛЬНИКА: '))
rectangle_y2 = float(input('Введите y правой верхней точки ПРЯМОУГОЛЬНИКА: '))

print('**********************************')
# окружность
circle_x = float(input('Введите x центра ОКРУЖНОСТИ: '))
circle_y = float(input('Введите y центра ОКРУЖНОСТИ: '))
circle_r = float(input('Введите радиус ОКРУЖНОСТИ: '))

print('**********************************')
# точка
x = float(input('Введите x точки: '))
y = float(input('Введите y точки: '))

print('############################################################################')
# прямая: y = kx + b
# окружность: (x - x0)^2 + (y - y0)^2 = r^2
# прямоугольник: x1, x2, y1, y2


def line(x, y):
    if k == 'undef':
        if x < line_x1:
            return 'слева'
        elif x > line_x1:
            return 'справа'
    elif y < k*x+b:
        return '<'
    elif y > k*x+b:
        return '>'
    else:
        return '='


def circle(x, y):
    if (x - circle_x)**2 + (y - circle_y)**2 < circle_r**2:
        return 'in'
    elif (x - circle_x)**2 + (y - circle_y)**2 > circle_r**2:
        return 'out'
    else:
        return '='


def rectangle(x, y):
    if x > rectangle_x1 and x < rectangle_x2 and y > rectangle_y1 and y < rectangle_y2:
        return 'in'
    if x < rectangle_x1 or x > rectangle_x2 or y < rectangle_y1 or y > rectangle_y2:
        return 'out'
    else:
        return '='


# позиция относительно прямой
line_status = line(x, y)
if line_status == '>':
    print(f'точка с координатами ({x};{y}) находится выше прямой y = {k}*x + {b}')
elif line_status == '<':
    print(f'точка с координатами ({x};{y}) находится ниже прямой y = {k}*x + {b}')
elif line_status == 'слева':
    print(f'точка с координатами ({x};{y}) находится слева от прямой y = {k}*x + {b}')
elif line_status == 'справа':
    print(f'точка с координатами ({x};{y}) находится справа от прямой y = {k}*x + {b}')
elif line_status == '=':
    print(f'точка с координатами ({x};{y}) находится на прямой y = {k}*x + {b}')

# позиция относительно окружности
circle_status = circle(x, y)
if circle_status == 'in':
    print(f'точка с координатами ({x};{y}) находится внутри окружности (x - {circle_x})\u00b2 + (y - {circle_y})\u00b2 = {circle_r}\u00b2')
elif circle_status == 'out':
    print(f'точка с координатами ({x};{y}) находится вне окружности (x - {circle_x})\u00b2 + (y - {circle_y})\u00b2 = {circle_r}\u00b2')
elif circle_status == '=':
    print(f'точка с координатами ({x};{y}) находится на окружности (x - {circle_x})\u00b2 + (y - {circle_y})\u00b2 = {circle_r}\u00b2')

# позиция относительно прямоугольника
rectangle_status = rectangle(x, y)
if rectangle_status == 'in':
    print(f'точка с координатами ({x};{y}) находится внутри прямоугольника')
elif rectangle_status == 'out':
    print(f'точка с координатами ({x};{y}) находится вне прямоугольника')
elif rectangle_status == '=':
    print(f'точка с координатами ({x};{y}) лежит на ребре прямоугольника')

print('############################################################################')
