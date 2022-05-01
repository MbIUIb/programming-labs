import pygame
import sys
from programming_languages_labs.Lab8.lab8 import lab_8


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


lab_8(circle_x=0, circle_y=0)

W = 650  # ширина экрана
H = 500  # высота экрана
WHITE = (255, 255, 255)
icon = pygame.image.load('img.png')
pygame.display.set_caption('Lab9')
pygame.display.set_icon(icon)
sc = pygame.display.set_mode((W, H))
# clock = pygame.time.Clock()

while 1:
    lab_8(circle_x, circle_y)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                circle_x -= 1
            elif i.key == pygame.K_d:
                circle_x += 1
            elif i.key == pygame.K_w:
                circle_y += 1
            elif i.key == pygame.K_s:
                circle_y -= 1
            else:
                print('Нажатая клавиша не поддерживается...')

    sc.fill(WHITE)
    fig_surf = pygame.image.load('fig.png')
    fig_rect = fig_surf.get_rect(
        bottomright=(W, H))
    sc.blit(fig_surf, fig_rect)
    pygame.display.update()
