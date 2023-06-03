import pygame
from settings import *
from collections import deque  # позволяет с огромной скоростью перемещать элементы массива из начала в конец (rotate())


class Sprites:
    def __init__(self):
        # Характеристики спрайтов в словаре, ключ - название спрайта, зн-ние - словарь с его параметрами
        self.sprite_parameters = {
            'sprite_barrel': {
                'sprite': pygame.image.load('sprites/barrel/base/0.png').convert_alpha(),  # спрайт(ы) из базовой папки
                'viewing_angles': None,  # переименованный параметр статик (имеются ли углы обзора у спрайта)
                'shift': 1.8,  # сдвиг
                'scale': 0.4,  # масштаб
                'animation': deque([pygame.image.load(f'sprites/barrel/anim/{i}.png').convert_alpha()
                                    for i in range(12)]),  # анимация (очередь из всех спрайтов, или ложное значение)
                'animation_dist': 800,  # расстояние до спрайта, при котором включается его анимация
                'animation_speed': 10,  # скорости анимации
                'blocked': True,  # сами определяем, какие спрайты проходимы, а какие - нет
            },
            'sprite_pin': {
                'sprite': pygame.image.load('sprites/pin/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': 0.6,
                'animation': deque([pygame.image.load(f'sprites/pin/anim/{i}.png').convert_alpha() for i in range(8)]),
                'animation_dist': 800,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_devil': {
                'sprite': [pygame.image.load(f'sprites/devil/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': -0.2,
                'scale': 1.1,
                'animation': deque(
                    [pygame.image.load(f'sprites/devil/anim/{i}.png').convert_alpha() for i in range(9)]),
                'animation_dist': 150,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_flame': {
                'sprite': pygame.image.load('sprites/flame/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'sprites/flame/anim/{i}.png').convert_alpha() for i in range(16)]),
                'animation_dist': 800,
                'animation_speed': 5,
                'blocked': False,  # пламя проходимое
            },
        }
        # Тут держим все спрайтовые картинки для текущей карты, т.е. это карта наших спрайтов
        self.list_of_objects = [
            SpriteObject(self.sprite_parameters['sprite_barrel'], (7.1, 2.1)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (5.9, 2.1)),
            SpriteObject(self.sprite_parameters['sprite_pin'], (8.7, 2.5)),
            SpriteObject(self.sprite_parameters['sprite_devil'], (7, 4)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (8.6, 5.6))
        ]  # чтобы разместить спрайт, достаточно передать словарь по ключу и его местоположение на карте


# Местоположение спрайта и его проекционные характеристики
class SpriteObject:
    # (тип спрайта, явл.ли стат.картинкой, без углов обзора/нет, положение на карте, сдвиг по вертикали при масштабиров)
    def __init__(self, parameters, pos):
        # инициализируем атрибуты по установленным параметрам для спрайтов (по доступу по ключам)
        self.object = parameters['sprite']
        self.viewing_angles = parameters['viewing_angles']
        self.shift = parameters['shift']  # сдвиг по высоте
        self.scale = parameters['scale']  # для масштабирования картинки
        self.animation = parameters['animation'].copy()
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.blocked = parameters['blocked']
        self.side = 30  # определим сторону квадрата, в котором будет спрайт
        self.animation_count = 0  # счётчик для реализации нашей анимации
        self.x, self.y = pos[0] * TILE, pos[1] * TILE  # координаты спрайта задаем в системе координат карты
        self.pos = self.x - self.side // 2, self.y - self.side // 2  # положение спрайта в центре этого квадрата
        if self.viewing_angles:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    # (экземпляр класса Игрок, словарь с номерами лучей и расстояниями до стен)
    def object_locate(self, player):
        dx, dy = self.x - player.x, self.y - player.y  # разности координат между игроком и спрайтом
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)  # расстояние до спрайта

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        # Эмпирическим путем выводим угол гамма, будет находиться в нужных нам пределах для вычислений
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
        if 0 <= fake_ray <= FAKE_RAYS_RANGE and distance_to_sprite > 30:
            proj_height = min(int(PROJ_COEFF / distance_to_sprite * self.scale), DOUBLE_HEIGHT)  # проекц высота спрайта
            half_proj_height = proj_height // 2  # коэффициент масштабирования спрайта
            shift = half_proj_height * self.shift  # механизм регулирования спрайта по высоте

            # choosing sprite for angle (алгоритм выбора правильного спрайта в зависимости от угла тетта)
            if self.viewing_angles:
                if theta < 0:
                    theta += DOUBLE_PI  # корректируем угол, чтобы он находился в [0, 2п]
                theta = 360 - int(math.degrees(theta))

                # проходимся по списку с углами
                for angles in self.sprite_angles:
                    if theta in angles:  # как только угол попадет в один из диапазонов, нужным спрайтом
                        self.object = self.sprite_positions[angles]  # будет значение в словаре по ключу от этого угла
                        break

            # sprite animation
            sprite_object = self.object
            # если у спрайта есть анимация и расстояние до него меньше установленного значения,
            if self.animation and distance_to_sprite < self.animation_dist:
                sprite_object = self.animation[0]  # то будем отображать на экране 1-й спрайт в очереди
                if self.animation_count < self.animation_speed:
                    self.animation_count += 1  # столько раз, сколько заложено параметром скорости анимации
                else:  # как только счетчик операции станет равен параметру скорости
                    self.animation.rotate()  # то прокручиваем очередь методом
                    self.animation_count = 0  # и все те же самые действия будем проделывать с другим спрайтом

            """ Позиция спрайта относительно его луча, для этого совместили центр спрайта с его лучом, 
                и определим положение по высоте с учетом его заданного сдвига"""
            sprite_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)

            # масштабируем спрайт по размерам его проекционной высоте и отдаем на отрисовку
            sprite = pygame.transform.scale(sprite_object, (proj_height, proj_height))
            return distance_to_sprite, sprite, sprite_pos
        else:
            return False,
