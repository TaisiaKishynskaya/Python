import pygame
from settings import *
from collections import deque  # позволяет с огромной скоростью перемещать элементы массива из начала в конец (rotate())
from ray_casting import mapping
from numba.core import types
from numba.typed import Dict
from numba import int32


class Sprites:
    def __init__(self):
        # Характеристики спрайтов в словаре, ключ - название спрайта, зн-ние - словарь с его параметрами
        self.sprite_parameters = {
            'sprite_barrel': {
                'sprite': pygame.image.load('sprites/barrel/base/0.png').convert_alpha(),  # спрайт(ы) из базовой папки
                'viewing_angles': None,  # переименованный параметр статик (имеются ли углы обзора у спрайта)
                'shift': 1.8,  # сдвиг
                'scale': (0.4, 0.4),  # масштаб (у каждой оси свой коэфициент)
                'side': 30,  # размер
                'animation': deque([pygame.image.load(f'sprites/barrel/anim/{i}.png').convert_alpha()
                                    for i in range(12)]),  # анимация (очередь из всех спрайтов, или ложное значение)
                'death_animation': deque([pygame.image.load(f'sprites/barrel/death/{i}.png').convert_alpha()
                                          for i in range(4)]),  # анимация разрушения
                'is_dead': None,  # параметр, определяющий, жив или нет объект
                'dead_shift': 2.6,  # сдвиг спрайта после его гибели
                'animation_dist': 800,  # расстояние до спрайта, при котором включается его анимация
                'animation_speed': 10,  # скорости анимации
                'blocked': True,  # сами определяем, какие спрайты проходимы, а какие - нет
                'flag': 'decor',  # тип спрайта
                'obj_action': []  # параметр, отвечающий за действие при виде игрока
            },
            'sprite_pin': {
                'sprite': pygame.image.load('sprites/pin/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': (0.6, 0.6),
                'side': 30,
                'animation': deque([pygame.image.load(f'sprites/pin/anim/{i}.png').convert_alpha() for i in range(8)]),
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': None,
                'animation_dist': 800,
                'animation_speed': 10,
                'blocked': True,
                'flag': 'decor',
                'obj_action': []
            },
            'sprite_flame': {
                'sprite': pygame.image.load('sprites/flame/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': (0.6, 0.6),
                'side': 30,
                'animation': deque(
                    [pygame.image.load(f'sprites/flame/anim/{i}.png').convert_alpha() for i in range(16)]),
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': 1.8,
                'animation_dist': 1800,
                'animation_speed': 5,
                'blocked': None,
                'flag': 'decor',
                'obj_action': []
            },
            'npc_devil': {
                'sprite': [pygame.image.load(f'sprites/devil/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 0.0,
                'scale': (1.1, 1.1),
                'side': 50,
                'animation': [],
                'death_animation': deque([pygame.image.load(f'sprites/devil/death/{i}.png').convert_alpha()
                                          for i in range(6)]),
                'is_dead': None,
                'dead_shift': 0.6,
                'animation_dist': None,
                'animation_speed': 10,
                'blocked': True,
                'flag': 'npc',
                'obj_action': deque(
                    [pygame.image.load(f'sprites/devil/anim/{i}.png').convert_alpha() for i in range(9)]),
            },
            'sprite_door_v': {
                'sprite': [pygame.image.load(f'sprites/doors/door_v/{i}.png').convert_alpha() for i in range(16)],
                'viewing_angles': True,
                'shift': 0.1,
                'scale': (2.6, 1.2),
                'side': 100,
                'animation': [],
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': 0,
                'animation_dist': 0,
                'animation_speed': 0,
                'blocked': True,
                'flag': 'door_h',
                'obj_action': []
            },
            'sprite_door_h': {
                'sprite': [pygame.image.load(f'sprites/doors/door_h/{i}.png').convert_alpha() for i in range(16)],
                'viewing_angles': True,
                'shift': 0.1,
                'scale': (2.6, 1.2),
                'side': 100,
                'animation': [],
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': 0,
                'animation_dist': 0,
                'animation_speed': 0,
                'blocked': True,
                'flag': 'door_v',
                'obj_action': []
            },
            'npc_soldier0': {
                'sprite': [pygame.image.load(f'sprites/npc/soldier0/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 0.8,
                'scale': (0.4, 0.6),
                'side': 30,
                'animation': [],
                'death_animation': deque([pygame.image.load(f'sprites/npc/soldier0/death/{i}.png').convert_alpha()
                                          for i in range(10)]),
                'is_dead': None,
                'dead_shift': 1.7,
                'animation_dist': None,
                'animation_speed': 6,
                'blocked': True,
                'flag': 'npc',
                'obj_action': deque([pygame.image.load(f'sprites/npc/soldier0/action/{i}.png').convert_alpha()
                                     for i in range(4)])
            },
        }

        # Тут держим все спрайтовые картинки для текущей карты, т.е. это карта наших спрайтов
        # чтобы разместить спрайт, достаточно передать словарь по ключу и его местоположение на карте
        self.list_of_objects = [SpriteObject(self.sprite_parameters['sprite_barrel'], (7.1, 2.1)),
                                SpriteObject(self.sprite_parameters['sprite_barrel'], (5.9, 2.1)),
                                SpriteObject(self.sprite_parameters['sprite_pin'], (8.7, 2.5)),
                                SpriteObject(self.sprite_parameters['npc_devil'], (7, 4)),
                                SpriteObject(self.sprite_parameters['sprite_flame'], (8.6, 5.6)),
                                SpriteObject(self.sprite_parameters['sprite_door_v'], (3.5, 3.5)),  # посередине клеток
                                SpriteObject(self.sprite_parameters['sprite_door_h'], (1.5, 4.5)),  # посередине клеток
                                SpriteObject(self.sprite_parameters['npc_soldier0'], (2.5, 1.5)),
                                SpriteObject(self.sprite_parameters['npc_soldier0'], (5.51, 1.5)),
                                SpriteObject(self.sprite_parameters['npc_soldier0'], (6.61, 2.92)),
                                SpriteObject(self.sprite_parameters['npc_soldier0'], (7.68, 1.47)),
                                SpriteObject(self.sprite_parameters['npc_soldier0'], (8.75, 3.65)),
                                SpriteObject(self.sprite_parameters['npc_soldier0'], (1.27, 11.5)),
                                SpriteObject(self.sprite_parameters['npc_soldier0'], (1.26, 8.29))]

    # механизм для определения спрайта, который находится под выстрелом
    @property
    def sprite_shot(self):  # вернет ближайший спрайт и если таких спрайтов много под выстрелом
        return min([obj.is_on_fire for obj in self.list_of_objects], default=(float('inf'), 0))

    # Ф-я возврата словаря всех закрытых дверей на карте
    @property
    def blocked_doors(self):
        # импорт из numba, так как его необходимо использовать в ray_casting_npc_player
        blocked_doors = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
        for obj in self.list_of_objects:
            if obj.flag in {'door_h', 'door_v'} and obj.blocked:
                i, j = mapping(obj.x, obj.y)
                blocked_doors[(i, j)] = 0
        return blocked_doors


# Местоположение спрайта и его проекционные характеристики
class SpriteObject:
    # (тип спрайта, явл.ли стат.картинкой, без углов обзора/нет, положение на карте, сдвиг по вертикали при масштабиров)
    def __init__(self, parameters, pos):
        # инициализируем атрибуты по установленным параметрам для спрайтов (по доступу по ключам)
        self.object = parameters['sprite'].copy()
        self.viewing_angles = parameters['viewing_angles']
        self.shift = parameters['shift']  # сдвиг по высоте
        self.scale = parameters['scale']  # для масштабирования картинки
        self.animation = parameters['animation'].copy()  # в любом атрибуте, связанным с анимацией, чтобы не было багов

        self.death_animation = parameters['death_animation'].copy()
        self.is_dead = parameters['is_dead']
        self.dead_shift = parameters['dead_shift']

        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.blocked = parameters['blocked']
        self.flag = parameters['flag']
        self.obj_action = parameters['obj_action'].copy()
        self.x, self.y = pos[0] * TILE, pos[1] * TILE  # координаты спрайта задаем в системе координат карты
        self.side = parameters['side']  # определим сторону квадрата, в котором будет спрайт
        self.dead_animation_count = 0  # счётчик для функционирования анимации смерти объектов
        self.animation_count = 0  # счётчик для реализации нашей анимации
        self.npc_action_trigger = False  # триггер для выполнения действия объекта
        self.door_open_trigger = False  # триггер для открытия дверей
        # зн-ние предыдущего положения двери (для анимации открытия):
        self.door_prev_pos = self.y if self.flag == 'door_h' else self.x
        self.delete = False  # параметр для удаления объекта
        if self.viewing_angles:
            if len(self.object) == 8:
                self.sprite_angles = [frozenset(range(338, 361)) | frozenset(range(0, 23))] + \
                                     [frozenset(range(i, i + 45)) for i in range(23, 338, 45)]
            else:  # т.к. углов обзора дверей 16, делаем соотв. список углов для таких объектов
                self.sprite_angles = [frozenset(range(348, 361)) | frozenset(range(0, 11))] + \
                                     [frozenset(range(i, i + 23)) for i in range(11, 348, 23)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}
        self.distance_to_sprite = 0  # Инициализация атрибута distance_to_sprite
        self.theta = 0  # Инициализация атрибута theta
        self.current_ray = 0  # Инициализация атрибута current_ray
        self.proj_height = 0  # Инициализация атрибута proj_height
        self.dead_sprite = 0   # Инициализация атрибута dead_sprite

    # Св-во, которое вернет расстояние и проекцию спрайта, что нах. под огнем
    @property
    def is_on_fire(self):
        # Если спрайт нах. на центр. луче и в еще небольшом диапазоне лучей от него, то его считаем спрайтом под огнем
        if CENTER_RAY - self.side // 2 < self.current_ray < CENTER_RAY + self.side // 2 and self.blocked:
            return self.distance_to_sprite, self.proj_height
        return float('inf'), None

    @property
    def pos(self):
        return self.x - self.side // 2, self.y - self.side // 2

    # (экземпляр класса Игрок, словарь с номерами лучей и расстояниями до стен)
    def object_locate(self, player):

        dx, dy = self.x - player.x, self.y - player.y  # разности координат между игроком и спрайтом
        self.distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)  # расстояние до спрайта

        self.theta = math.atan2(dy, dx)
        gamma = self.theta - player.angle
        # Эмпирическим путем выводим угол гамма, будет находиться в нужных нам пределах для вычислений
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI  # корректируем угол гамма на 2п, в зависимости от направления игрока
        self.theta -= 1.4 * gamma

        delta_rays = int(gamma / DELTA_ANGLE)  # смещение спрайта относительно центрального луча
        """корректируем расстояние до спрайта, чтобы не было эффекта рыбьего глаза, 
           иначе спрайт будет перемещаться не ровно, а по дуге"""
        self.current_ray = CENTER_RAY + delta_rays
        # условия выполнения некоторых вычислений для дверей (делаем, ибо не вынесли это в отдельный класс)
        if self.flag not in {'door_h', 'door_v'}:
            self.distance_to_sprite *= math.cos(HALF_FOV - self.current_ray * DELTA_ANGLE)

        fake_ray = self.current_ray + FAKE_RAYS  # возможность отображать спрайт на фейк лучах за пределами экрана
        """Попадает ли луч, на котором нах. спрайт, в наш диапазон лучей, а также если на том же луче есть препятствия,
           то выясним, будет ли спрайт ближе к нам, чем стена"""
        if 0 <= fake_ray <= FAKE_RAYS_RANGE and self.distance_to_sprite > 30:
            # проекц высота спрайта:
            self.proj_height = min(int(PROJ_COEF / self.distance_to_sprite),
                                   DOUBLE_HEIGHT if self.flag not in {'door_h', 'door_v'} else HEIGHT)
            # для адекватного масштабирования спрайта по двум осям:
            sprite_width = int(self.proj_height * self.scale[0])
            sprite_height = int(self.proj_height * self.scale[1])
            # сохраняем механизм сдвига спрайта по оси у для масштабирования любого спрайта без искажения:
            half_sprite_width = sprite_width // 2
            half_sprite_height = sprite_height // 2  # коэффициент масштабирования спрайта
            shift = half_sprite_height * self.shift  # механизм регулирования спрайта по высоте

            # logic for doors, npc, decor
            if self.flag in {'door_h', 'door_v'}:
                if self.door_open_trigger:  # если сработал триггер для двери
                    self.open_door()  # запускаем ф-ю открытия двери
                self.object = self.visible_sprite()
                sprite_object = self.sprite_animation()
            else:
                # логика, по которой вкл анимация смерти:
                if self.is_dead and self.is_dead != 'immortal':
                    sprite_object = self.dead_animation()
                    shift = half_sprite_height * self.dead_shift
                    sprite_height = int(sprite_height / 1.3)
                # логика, по которой вкл анимация взаимодействия с игроком:
                elif self.npc_action_trigger:
                    sprite_object = self.npc_in_action()
                # логика, по которой вкл первоначальная анимация для спрайтов:
                else:
                    self.object = self.visible_sprite()
                    sprite_object = self.sprite_animation()

            """ Позиция спрайта относительно его луча, для этого совместили центр спрайта с его лучом, 
                и определим положение по высоте с учетом его заданного сдвига"""
            sprite_pos = (self.current_ray * SCALE - half_sprite_width, HALF_HEIGHT - half_sprite_height + shift)
            # масштабируем спрайт по размерам его проекционной высоте и отдаем на отрисовку
            sprite = pygame.transform.scale(sprite_object, (sprite_width, sprite_height))
            return self.distance_to_sprite, sprite, sprite_pos
        else:
            return False,

    def sprite_animation(self):
        # если у спрайта есть анимация и расстояние до него меньше установленного значения,
        if self.animation and self.distance_to_sprite < self.animation_dist:
            sprite_object = self.animation[0]  # то будем отображать на экране 1-й спрайт в очереди
            if self.animation_count < self.animation_speed:
                self.animation_count += 1  # столько раз, сколько заложено параметром скорости анимации
            else:  # как только счетчик операции станет равен параметру скорости
                self.animation.rotate()  # то прокручиваем очередь методом
                self.animation_count = 0  # и все те же самые действия будем проделывать с другим спрайтом
            return sprite_object
        return self.object

    # ф-я определения правильного угла обзора для спрайта
    def visible_sprite(self):
        if self.viewing_angles:
            if self.theta < 0:
                self.theta += DOUBLE_PI
            self.theta = 360 - int(math.degrees(self.theta))

            for angles in self.sprite_angles:
                if self.theta in angles:
                    return self.sprite_positions[angles]
        return self.object

    # анимация смерти
    def dead_animation(self):
        if len(self.death_animation):
            if self.dead_animation_count < self.animation_speed:
                self.dead_sprite = self.death_animation[0]
                self.dead_animation_count += 1
            else:
                self.dead_sprite = self.death_animation.popleft()
                self.dead_animation_count = 0
        return self.dead_sprite

    # анимация взаимодействия npc с игроком
    def npc_in_action(self):
        sprite_object = self.obj_action[0]
        if self.animation_count < self.animation_speed:
            self.animation_count += 1
        else:
            self.obj_action.rotate()
            self.animation_count = 0
        return sprite_object

    # Ф-я открытия дверей
    def open_door(self):
        # в зависимости от типа дверей,
        if self.flag == 'door_h':
            self.y -= 3  # она будет уходить в стену со скоростью
            if abs(self.y - self.door_prev_pos) > TILE:  # и после того, как дверь пройдет расстояние > размера клетки
                self.delete = True  # удалим дверь с карты
        elif self.flag == 'door_v':
            self.x -= 3
            if abs(self.x - self.door_prev_pos) > TILE:
                self.delete = True
