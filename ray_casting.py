import pygame
from settings import *
from map import world_map, WORLD_WIDTH, WORLD_HEIGHT
from numba import njit
"""У пайтона низкая скорость работы. -> Numba - JIT компилятор, который переводит код на пайтоне в быстрый машинный код. 
Применяется в основном к функциям. Эти ф-ии нужно формировать по определенным правилам, где есть ряд ограничений.
Например, Numba не умеет работать с классами (только с ф-ми) и со стандартными словарями."""


# координаты верхнего левого угла квадрата, в котором мы находимся в данный момент
@njit(fastmath=True)
def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


"""В 1-й ф-ии основные вычисления, ускоряем ее при помощи @njit. В ней создаем список необходимых параметров для
формирования текстур во 2-й ф-ии. В ускоренную ф-ю помещать как можно больше вычислений"""


@njit(fastmath=True)
def ray_casting(player_pos, player_angle, world_map):
    casted_walls = []
    ox, oy = player_pos  # начальные координаты луча

    # Это избавит нас от ошибки в случае выхода за пределы карты:
    texture_v, texture_h = 1, 1  # дефолтные номера текстур для горизонтальных, вертикальных стен
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV  # текущий угол

    # цикл по всем лучам с реализацией алгоритма Бразенхэма:
    for ray in range(NUM_RAYS):  # вычисление тригонометрических ф-й направления луча
        sin_a = math.sin(cur_angle)  # определяет верхнее и нижнее направление горизонталей
        cos_a = math.cos(cur_angle)  # косинус определяет, в какую сторону идти по вертикалям
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        """в зависимости от знака косинуса, определим х - текущую вертикаль, dx - вспомогательная переменная, 
        при помощи которой будем получать очередную вертикаль."""
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        # проходимся по всем вертикалям (ширине экрана) с шагом = стороне квадрату карты
        for i in range(0, WORLD_WIDTH, TILE):
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
        for i in range(0, WORLD_HEIGHT, TILE):
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
        proj_height = min(int(PROJ_COEFF / depth), PENTA_HEIGHT)  # проекционная высота стены..

        # для каждого луча в список заносим параметры: дальность до стены, сдвиг по текстуре, пр.высота стены, №текстуры
        casted_walls.append((depth, offset, proj_height, texture))
        cur_angle += DELTA_ANGLE  # изменение угла для очередного луча
    return casted_walls


"""Главная задача - избавиться от экземпляров классов от pygame.
То есть вынести расчеты формирования текстур в отдельной ф-ии.
2-я ф-я работает только с текстурами, т.е. формирование подповерхности, её масштабирование, расчет позиции."""


def ray_casting_walls(player, textures):
    casted_walls = ray_casting(player.pos, player.angle, world_map)
    walls = []
    for ray, casted_values in enumerate(casted_walls):
        depth, offset, proj_height, texture = casted_values

        """Выделим подповерхность из нашей текстуры в виде квадрата, в котором начальные координаты равны 
        вычисленному смещению текстуры, а ширину и высоту возьмем из определенных нами настроек:"""
        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)

        """Масштабируем только что выделенную часть текстуры в прямоугольник, 
        размер которого мы использовали до этого, то есть учитывая величину проекции стены:"""
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))

        # Вернем список с параметрами как дальность до стены, рассчитанная область текстуры и ее расположение
        wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)  # это всё для зэт-буфера
        walls.append((depth, wall_column, wall_pos))
    return walls
