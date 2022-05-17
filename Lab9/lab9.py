import pygame
import sys
from programming_languages_labs.Lab8.lab8 import lab_8
from programming_languages_labs.Lab10.lab10 import Logger


log = Logger(file='Data\\lab9_logs.txt')
print(log.key)


with open('Data\\fig.txt') as f:
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


W = 650  # ширина экрана
H = 500  # высота экрана
WHITE = (255, 255, 255)
icon = pygame.image.load('Data\\img.png')
pygame.display.set_caption('Lab9')
pygame.display.set_icon(icon)
sc = pygame.display.set_mode((W, H))

while 1:
    lab_8(circle_x, circle_y)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            log.encrypt()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                circle_x -= 1
                log.new_log(f'circle_x -= 1 ({circle_x})')
            elif i.key == pygame.K_d:
                circle_x += 1
                log.new_log(f'circle_x += 1 ({circle_x})')
            elif i.key == pygame.K_w:
                circle_y += 1
                log.new_log(f'circle_y += 1 ({circle_y})')
            elif i.key == pygame.K_s:
                circle_y -= 1
                log.new_log(f'circle_x -= 1 ({circle_y})')
            else:
                print('Нажатая клавиша не поддерживается...')
                log.new_log(f'нажатие не поддерживаемой клавищи (key code: {i.key})')

    sc.fill(WHITE)
    fig_surf = pygame.image.load('Data\\fig.png')
    fig_rect = fig_surf.get_rect(bottomright=(W, H))
    sc.blit(fig_surf, fig_rect)
    pygame.display.update()
