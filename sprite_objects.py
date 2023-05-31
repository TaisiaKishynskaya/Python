import pygame
from settings import *


class Sprites:
    def __init__(self):
        self.sprite_types = {  # типы спрайтов в словаре, ключи соответствуют названиям картинок
            'barrel': pygame.image.load('sprites/barrel/0.png').convert_alpha(),
            'pedestal': pygame.image.load('sprites/pedestal/0.png').convert_alpha(),
            'devil': [pygame.image.load(f'sprites/devil/{i}.png').convert_alpha() for i in range(8)]}
        # тут держим все спрайтовые картинки для текущей карты, т.е. это карта наших спрайтов
        self.list_of_objects = [
            SpriteObject(self.sprite_types['barrel'], True, (7.1, 2.1), 1.8, 0.4),
            SpriteObject(self.sprite_types['barrel'], True, (5.9, 2.1), 1.8, 0.4),
            SpriteObject(self.sprite_types['pedestal'], True, (8.8, 2.5), 1.6, 0.5),
            SpriteObject(self.sprite_types['pedestal'], True, (8.8, 5.6), 1.6, 0.5),
            SpriteObject(self.sprite_types['devil'], False, (7, 4), -0.2, 0.7),
        ]


# Местоположение спрайта и его проекционные характеристики
class SpriteObject:
    # (тип спрайта, явл.ли стат.картинкой, без углов обзора/нет, положение на карте, сдвиг по вертикали при масштаб)
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE  # координаты спрайта задаем в системе координат карты
        self.shift = shift  # сдвиг по высоте
        self.scale = scale  # для масштабирования картинки

        if not static:
            # формируем диапазоны углов для каждого спрайта. 8 картинок - на каждый диапазон 45 градусов
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            # т.к это ключи в словаре. для быстрого поиска используем замороженные множества
            # обычное мн-во не получится использовать из-за того, что это изменяемый тип данных и ключами быть не могут
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    # (экземпляр класса Игрок, словарь с номерами лучей и расстояниями до стен)
    def object_locate(self, player, walls):
        fake_walls0 = [walls[0] for i in range(FAKE_RAYS)]  # фейк.лучи со значением параметров от первого стоящего луча
        fake_walls1 = [walls[-1] for i in range(FAKE_RAYS)]  # фейк.лучи со значением параметров от последнего луча
        fake_walls = fake_walls0 + walls + fake_walls1  # добавим слева и справа эти списки к основному списку стен ->

        dx, dy = self.x - player.x, self.y - player.y  # разности координат между игроком и спрайтом
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)  # расстояние до спрайта

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        # Эмпирическим путем выводим угол гамма будет нах. в нужных нам пределах для вычислений
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI  # корректируем угол гамма на 2п, в зависимости от направления игрока

        delta_rays = int(gamma / DELTA_ANGLE)  # смещение спрайта относительно центрального луча
        current_ray = CENTER_RAY + delta_rays
        """корректируем расстояние до спрайта, чтобы не было эффекта рыбьего глаза, 
        иначе спрайт будет перемещаться не ровно, а по дуге"""
        distance_to_sprite *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS  # -> получим возможность отображать спрайт на фейк лучах за пределами экрана
        """Попадает ли луч, на котором нах. спрайт, в наш диапазон лучей, а также если на том же луче есть препятствия,
        то выясним, будет ли спрайт ближе к нам, чем стена"""
        if 0 <= fake_ray <= NUM_RAYS - 1 + 2 * FAKE_RAYS and distance_to_sprite < fake_walls[fake_ray][0]:
            proj_height = min(int(PROJ_COEFF / distance_to_sprite * self.scale), 2 * HEIGHT)  # проекцион высота спрайта
            half_proj_height = proj_height // 2  # коефициент масштабирования спрайта
            shift = half_proj_height * self.shift  # механизм регулирования спрайта по высоте

            # алгоритм выбора правильного спрайта в зависимости от угла тетта
            if not self.static:
                if theta < 0:
                    theta += DOUBLE_PI  # корректируем угол, чтобы он находился в [0, 2п]
                theta = 360 - int(math.degrees(theta))

                # проходимсяя по списку с углами
                for angles in self.sprite_angles:
                    if theta in angles:  # как только угол попадет в один из диапазонов, нужным спрайтом
                        self.object = self.sprite_positions[angles]  # будет значение в словаре по ключу от этого угла
                        break

            """ Позиция спрайта относительно его луча, для этого совместили центр спрайта с его лучом, 
            и определим положение по высоте с учетом его заданного сдвига"""
            sprite_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            # масштабируем спрайт по размерам его проекции
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            return distance_to_sprite, sprite, sprite_pos
        else:
            return False,
