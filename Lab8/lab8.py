from matplotlib import pyplot as plt
import numpy as np

with open('fig.txt') as f:
    # прямая
    line_x1, line_y1, line_x2, line_y2 = map(float, f.readline().split())
    if line_x1 != line_x2:
        k = (line_y1 - line_y2) / (line_x1 - line_x2)
        b = line_y1 - k * line_x1
    else:
        k = 'undef'
    # прямоугольник
    rectangle_x1, rectangle_y1, rectangle_x2, rectangle_y2 = map(float, f.readline().split())
    # окружность
    circle_x, circle_y, circle_r = map(float, f.readline().split())
    # точка
    x, y = map(float, f.readline().split())


def lab_8(circle_x=0, circle_y=0):
    # функции, определяющие позиции относительно фигур
    def line_status(x, y):
        if k == 'undef':
            if x < line_x1:
                return 'слева'
            elif x > line_x1:
                return 'справа'
        elif y < k * x + b:
            return '<'
        elif y > k * x + b:
            return '>'
        else:
            return '='

    def circle_status(x, y):
        if (x - circle_x) ** 2 + (y - circle_y) ** 2 < circle_r ** 2:
            return 'in'
        elif (x - circle_x) ** 2 + (y - circle_y) ** 2 > circle_r ** 2:
            return 'out'
        else:
            return '='

    def rectangle_status(x, y):
        if x > rectangle_x1 and x < rectangle_x2 and y > rectangle_y1 and y < rectangle_y2:
            return 'in'
        if x < rectangle_x1 or x > rectangle_x2 or y < rectangle_y1 or y > rectangle_y2:
            return 'out'
        else:
            return '='

    line_status = line_status(x, y)
    circle_status = circle_status(x, y)
    rectangle_status = rectangle_status(x, y)
    scale = 15
    major_ticks = np.arange(-15, 14, 5)
    minor_ticks = np.arange(-15, 14, 1)

    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    def draw_line(x1=1, y1=1, x2=5, y2=5, draw='', color='#ff5d40'):
        """
        Строит прямую при draw=''
        Закрашивает область {справа/слева/сверху/снизу} при draw='справа/слева/сверху/снизу'
        color - цвет области
        """
        if k == 'undef':
            if draw == '':
                axes.plot([x1, x2], [-scale, scale], color='#33cccc')

            if draw == 'справа':
                x = np.linspace(x1, scale)
                # вспомогательные прямые
                line_y_top = [scale + 5] * len(x)
                line_y_bottom = [-(scale + 5)] * len(x)
                # axes.plot(x, line_y_top, 'k')
                # axes.plot(x, line_y_bottom, 'k')
                axes.fill_between(x, line_y_top, line_y_bottom, facecolor=color)

            if draw == 'слева':
                x = np.linspace(-scale, x1)
                # вспомогательные прямые
                line_y_top = [scale + 5] * len(x)
                line_y_bottom = [-(scale + 5)] * len(x)
                # axes.plot(x, line_y_top, 'k')
                # axes.plot(x, line_y_bottom, 'k')
                axes.fill_between(x, line_y_top, line_y_bottom, facecolor=color)

        else:
            x = np.linspace(-scale, scale)
            y = k * x + b

            if draw == '':
                axes.plot(x, y, color='#33cccc')

            if draw == '>':
                # вспомогательная прямая
                line_y_top = [scale + 5] * len(x)
                # axes.plot(x, line_y_top, 'w')
                axes.fill_between(x, line_y_top, y, facecolor=color)

            if draw == '<':
                # вспомогательная прямая
                line_y_bottom = [-(scale + 5)] * len(x)
                # axes.plot(x, line_y_bottom, 'w')
                axes.fill_between(x, line_y_bottom, y, facecolor=color)

    def draw_circle(x0=0, y0=0, r=4, draw='', color='#ff5d40'):
        """
        Выводит на экран окружность с центром в точке (x0, y0) и радиусом r при draw=''
        Закрашивает область {внутри/снаружи} окружности при draw='in/out'
        color - цвет области {внутри (draw='in') / вне (draw='out')} окружности
        """
        if draw == '':
            angle = np.linspace(0, 2 * np.pi, 180)
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            axes.plot(x + x0, y + y0, color='#39e639')
        if draw == 'in':
            draw_in = plt.Circle((x0, y0), r, color=color, fill=True)
            axes.add_patch(draw_in)
        if draw == 'out':
            x_top_1 = np.linspace(-scale, x0 - r)
            line_top_1 = [scale + 5] * len(x_top_1)
            line_bottom_1 = [-(scale + 5)] * len(x_top_1)
            axes.fill_between(x_top_1, line_top_1, line_bottom_1, facecolor=color)

            x_top_2 = np.linspace(x0 + r, scale)
            line_top_2 = [scale + 5] * len(x_top_2)
            line_bottom_2 = [-(scale + 5)] * len(x_top_2)
            axes.fill_between(x_top_2, line_top_2, line_bottom_2, facecolor=color)

            x_top_3 = np.linspace(x0 - r, x0 + r)
            line_top_3 = [scale + 5] * len(x_top_3)
            y_top = (r ** 2 - (x_top_3 - x0) ** 2) ** 0.5 + y0
            axes.plot(x_top_3, y_top)
            axes.fill_between(x_top_3, line_top_3, y_top, facecolor=color)

            x_top_4 = np.linspace(x0 - r, x0 + r)
            line_top_4 = [-(scale + 5)] * len(x_top_4)
            y_bottom = -(r ** 2 - (x_top_4 - x0) ** 2) ** 0.5 + y0
            axes.plot(x_top_4, y_bottom)
            axes.fill_between(x_top_4, line_top_4, y_bottom, facecolor=color)

    def draw_rectangle(x1=1, y1=2, x2=4, y2=6, draw='', color='#ff5d40'):
        """
        Выводит на экран прямоугольник с левой нижней точкой (x1, y1) и правой верхней точкой (x2, y2) при draw=''
        Закрашивает область {внутри/снаружи} прямоугольника при draw='in/out'
        color1 - цвет области {внутри (draw='in') / вне (draw='out')} прямоугольника
        color2 - цвет области внутри прямоугольника при draw='out'
        """
        # создание списков множеств точек x и y
        set_x = list(np.arange(x1, x2 + 1))
        set_y = list(np.arange(y1, y2 + 1))
        # определение прямых, задающих стороны прямоугольника
        line_y1 = [y1] * len(set_x)
        line_y2 = [y2] * len(set_x)
        line_x1 = [x1] * len(set_y)
        line_x2 = [x2] * len(set_y)
        if draw == '':
            axes.plot(set_x, line_y1, '#1142aa')  # прямая x = y1
            axes.plot(set_x, line_y2, '#1142aa')  # прямая x = y2
            axes.plot(line_x1, set_y, '#1142aa')  # прямая y = x1
            axes.plot(line_x2, set_y, '#1142aa')  # прямая y = x2
        if draw == 'in':
            axes.fill_between(set_x, line_y1, line_y2, facecolor=color)
        if draw == 'out':
            x_top_1 = np.linspace(-scale, x1)
            line_top_1 = [scale + 5] * len(x_top_1)
            line_bottom_1 = [-(scale + 5)] * len(x_top_1)
            axes.fill_between(x_top_1, line_top_1, line_bottom_1, facecolor=color)

            x_top_2 = np.linspace(x1, x2)
            line_top_2 = [scale + 5] * len(x_top_2)
            x_rect_top = [y2] * len(x_top_2)
            line_bottom_2 = [-(scale + 5)] * len(x_top_2)
            x_rect_bottom = [y1] * len(x_top_2)
            axes.fill_between(x_top_2, line_top_2, x_rect_top, facecolor=color)
            axes.fill_between(x_top_2, line_bottom_2, x_rect_bottom, facecolor=color)

            x_top_3 = np.linspace(x2, scale)
            line_top_3 = [scale + 5] * len(x_top_3)
            line_bottom_3 = [-(scale + 5)] * len(x_top_3)
            axes.fill_between(x_top_3, line_top_3, line_bottom_3, facecolor=color)

    def draw_scatter(x=2, y=4):
        """Рисует точку в точке (x, y)"""
        axes.scatter(x, y, 15, color='k', marker='x')
        # axes.scatter(x, y, 10, color='k', marker='x')

    # отрисовка фигур
    draw_line(line_x1, line_y1, line_x2, line_y2)
    draw_circle(circle_x, circle_y, circle_r)
    draw_rectangle(rectangle_x1, rectangle_y1, rectangle_x2, rectangle_y2)
    draw_scatter(x, y)

    # отрисовка области
    if circle_status == 'in' and rectangle_status == 'in':
        draw_line(line_x1, line_y1, line_x2, line_y2, line_status)
        draw_circle(circle_x, circle_y, circle_r, 'out', 'w')
        draw_rectangle(rectangle_x1, rectangle_y1, rectangle_x2, rectangle_y2, 'out', 'w')
    if circle_status == 'in' and rectangle_status == 'out':
        draw_line(line_x1, line_y1, line_x2, line_y2, line_status)
        draw_circle(circle_x, circle_y, circle_r, 'out', 'w')
        draw_rectangle(rectangle_x1, rectangle_y1, rectangle_x2, rectangle_y2, 'in', 'w')
    if circle_status == 'out' and rectangle_status == 'in':
        draw_line(line_x1, line_y1, line_x2, line_y2, line_status)
        draw_rectangle(rectangle_x1, rectangle_y1, rectangle_x2, rectangle_y2, 'out', 'w')
        draw_circle(circle_x, circle_y, circle_r, 'in', 'w')
    if circle_status == 'out' and rectangle_status == 'out':
        draw_line(line_x1, line_y1, line_x2, line_y2, line_status)
        draw_rectangle(rectangle_x1, rectangle_y1, rectangle_x2, rectangle_y2, 'in', 'w')
        draw_circle(circle_x, circle_y, circle_r, 'in', 'w')

    # повторная отрисовка фигур поверх заливок
    draw_line(line_x1, line_y1, line_x2, line_y2)
    draw_circle(circle_x, circle_y, circle_r)
    draw_rectangle(rectangle_x1, rectangle_y1, rectangle_x2, rectangle_y2)
    draw_scatter(x, y)

    # подписи на графике
    plt.title('Lab8')
    plt.figtext(0.01, 0.5,
                f'line status: {line_status}\ncircle status: {circle_status}\nrectangle status: {rectangle_status}',
                fontsize=8)

    # добавление легенды
    if k == 'undef':
        plt.legend(
            (f'x = {line_x1}', f'(x - {circle_x})\u00b2 + (y - {circle_y})\u00b2 = {circle_r}\u00b2', 'rectangle'))
    else:
        plt.legend(
            (f'y = {k}*x + {b}', f'(x - {circle_x})\u00b2 + (y - {circle_y})\u00b2 = {circle_r}\u00b2', 'rectangle'))

    # сдвиг осей x и y на центр, удаление видимости верхней и правой осей
    axes.spines['left'].set_position('center')
    axes.spines['bottom'].set_position('center')
    axes.spines['right'].set_visible(False)
    axes.spines['top'].set_visible(False)
    # стрелки направления осей
    plt.text(-1, 14, 'Y')
    plt.text(14, -2, 'X')
    axes.scatter(0, 14.7, color='k', marker='^')
    axes.scatter(14.7, 0, color='k', marker='>')
    # метки на осях
    axes.set_xticks(major_ticks)
    axes.set_xticks(minor_ticks, minor=True)
    axes.set_yticks(major_ticks)
    axes.set_yticks(minor_ticks, minor=True)
    # ограничение осей
    plt.xlim(left=-scale, right=scale)
    plt.ylim(bottom=-scale, top=scale)
    axes.set_aspect(1)  # отношение осей друг к другу
    # сетка графика
    axes.grid(which='minor', alpha=0.2)
    axes.grid(which='major', alpha=0.5)

    plt.savefig('fig.png')
    plt.close()

# lab_8()
