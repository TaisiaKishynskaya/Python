import pygame
from settings import *
from map import world_map

"""Ф-я принимает поверхности отрисовки, позицию и угол игрока"""


def ray_casting(sc, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV  # угол для первого луча
    xo, yo = player_pos  # начальные координаты всех лучей, по ним пройдемся в цикле
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)  # вычисляем синус направления лучей
        cos_a = math.cos(cur_angle)  # вычисляем косинус направления лучей
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            # pygame.draw.line(sc, DARKGRAY, player_pos, (x, y), 2)  # промежуточный результат

            """Проверка на попадание луча в карту"""
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                # Чтобы избежать эффекта рыбьего глаза, что возникает из-за использования евклидовых расстояний:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = min(PROJ_COEFF / (depth + 0.0001), HEIGHT)  # проекционная высота стены..
                c = 255 / (1 + depth * depth * 0.0001)  # глубина цвета, в зависимости от рассчитанного расстояния
                color = (c // 2, c, c // 3)
                """..изобразим ее в виде прямоугольника на каждом луче с использованием коеф. масштабирования.
                Так и превращаем 2д мир в 3д мир."""
                pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break  # обрываем цикл, потому что уже нашли расстояние до ближайшего объекта
        cur_angle += DELTA_ANGLE  # изменение угла для очередного луча
