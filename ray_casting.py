import pygame
from settings import *
from map import world_map


# координаты верхнего левого угла квадрата, в котором мы находимся в данный момент
def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


# Ф-я принимает поверхности отрисовки, позицию и угол игрока
def ray_casting(sc, player_pos, player_angle, textures):
    ox, oy = player_pos  # начальные координаты луча
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV  # текущий угол
    # цикл по всем лучам с реализацией алгоритма Бразенхэма:
    for ray in range(NUM_RAYS):  # вычисление тригонометрических ф-й направления луча
        sin_a = math.sin(cur_angle)  # определяет верхнее и нижнее направление горизонталей
        cos_a = math.cos(cur_angle)  # косинус определяет, в какую сторону идти по вертикалям

        # verticals
        """в зависимости от знака косинуса, определим х - текущую вертикаль, dx - вспомогательная переменная, 
        при помощи которой будем получать очередную вертикаль."""
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        # проходимся по всем вертикалям (ширине экрана) с шагом = стороне квадрату карты
        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a  # расстояние до вертикали
            yv = oy + depth_v * sin_a  # координата вертикали у по выведенным раннее формулам
            tile_v = mapping(x + dx, yv)
            """Когда мы натыкаемся на препятствие, то при помощи координат луча в этом месте 
            сразу же получаем номер необходимой текстуры:"""
            if tile_v in world_map:  # проверка на предмет столкновения со стеной
                texture_v = world_map[tile_v]  # определяем номер текстуры
                break  # если пересечения не было, то переходим к следующей вертикали
            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        # projection
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % TILE  # Вычислим смещение путем нахождения остатка от деления от квадрата карты
        # Чтобы избежать эффекта рыбьего глаза, что возникает из-за использования евклидовых расстояний:
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)  # избегаем падения игры из-за деления на 0
        # Падение фпс при приближении к стенам из-за отрисовки проекций большой величины, ограничим ее вот так:
        proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGHT)  # проекционная высота стены..

        """Выделим подповерхность из нашей текстуры в виде квадрата, в котором начальные координаты равны вычесленному 
        смещению текстуры, а ширину и высоту возьмем из определенных нами настроек:"""
        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        """Масштабируем только что выделенную часть текстуры в пямоугольник, 
        размер которого мы использовали до этого, то есть учитывая величину проекци стены:"""
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        """Наносим эту часть текстуры на главную поверхность в зависимости от нумерации луча"""
        sc.blit(wall_column, (ray * SCALE, HALF_HEIGHT - proj_height // 2))

        cur_angle += DELTA_ANGLE  # изменение угла для очередного луча
