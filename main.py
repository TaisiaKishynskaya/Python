import pygame
from settings import *
from player import Player
# import math
# from map import world_map
from ray_casting import ray_casting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))  # разрешение экрана
clock = pygame.time.Clock()  # объект класса Clock для установки кол-ва кадров в секунду
player = Player()

while True:
    for event in pygame.event.get():  # проверим все события
        if event.type == pygame.QUIT:  # на предмет закрытия окна и выхода из приложения
            exit()
    player.movement()  # управление игроком
    sc.fill(BLACK)  # поверхность чёрная, обновим содержимое приложения на каждой итерации

    pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HALF_HEIGHT))  # небо
    pygame.draw.rect(sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))  # пол

    ray_casting(sc, player.pos, player.angle)

    """Координаты дробные, поэтому передаем их целую часть в построении круга"""
    # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)  # игрок - круг в центре экрана

    """Вычислим синус и косинус направления угла игрока, направление задали отрисовкой линии, 
         длина которой равна ширине экрана"""
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                          player.y + WIDTH * math. sin(player.angle)), 2)

    """Это позволяет менять структуру карты в любой момент без лишних хлопот."""
    # for x,y in world_map:
    #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)  # пройдясь по х и у, рисуем соответствующие им квадраты

    pygame.display.flip()
    clock.tick(FPS)  # задержка для нужного ФПС
    # print(clock.get_fps())
