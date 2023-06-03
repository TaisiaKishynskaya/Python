from settings import *
import pygame
import math
from map import collision_walls

"""Для управления игроком"""


class Player:
    def __init__(self, sprites):
        self.x, self.y = PLAYER_POS  # координаты игрока
        self.sprites = sprites  # позволяет создать карту спрайтов
        self.angle = PLAYER_ANGLE  # направление взгляда
        self.sensitivity = 0.004  # чувствительность мышки

        # collision parameters
        self.side = 50  # размер стороны квадрата, который будет игроком на карте вместо точки
        self.rect = pygame.Rect(*PLAYER_POS, self.side, self.side)  # экземпляр класса Rect
        # weapon
        self.shot = False  # логический параметр, True при нажатии ЛКМ

    @property
    def pos(self):
        return self.x, self.y  # вернет позицию по х и у

    # Список всех объектов для коллизии, т.к. объекты меняют атрибуты блокировки
    @property
    def collision_list(self):
        return collision_walls + [pygame.Rect(*obj.pos, obj.side, obj.side) for obj in
                                  self.sprites.list_of_objects if obj.blocked]

    # Ф-я для определения столкновений, принимает передвижение на 1 шаг по обоим осям
    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()  # берем копию нашего текущего положения
        next_rect.move_ip(dx, dy)  # и переместим на dx, dy
        # формируем индекс стен, с которыми столкнулся игрок на гипотетическом шаге (collidelistall())
        hit_indexes = next_rect.collidelistall(self.collision_list)

        # в зависимости от столкновений
        if len(hit_indexes):
            delta_x, delta_y = 0, 0  # будем находить сторону, с которой столкнулись
            for hit_index in hit_indexes:  # коллизий может быть несколько
                hit_rect = self.collision_list[hit_index]
                if dx > 0:  # мы можем попасть в промежуток между двух стен, тогда нужно
                    delta_x += next_rect.right - hit_rect.left  # по двум стенам определить куда мы уперлись
                else:
                    delta_x += hit_rect.right - next_rect.left  # есть случай, когда мы зашли или наткнулись в угол
                if dy > 0:  # тогда мы будем полностью останавливаться
                    delta_y += next_rect.bottom - hit_rect.top
                else:  # условием этого есть примерное равенство между суммарными пересечениями
                    delta_y += hit_rect.bottom - next_rect.top

            """Решения принимаются в зависимости от значений delta_x и delta_y. 
            В них будет хранится суммарная величина пересечений по обоим осям. 
            На основе решений запрещаем игроку двигаться в объект столкновения. То есть с учетом этого.."""
            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0  # изменяем реальные координаты игрока и туда уже перемещаем центр квадрата
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx  # ..изменяем реальные координаты игрока и..
        self.y += dy

    """Мы - круг. У нас есть направление луча под углом а. Для каждой клавиши у нас перемещение d должно быть одинаково.
    Все направления отличаются на 90 градусов -> Применяем формулы приведения тригонометрических ф-й для того, чтобы
    найти создать управление подобное 3д, а не 2д."""

    # будет отслеживать нажатые клавиши и менять соответствующее значение атрибутов
    def movement(self):
        self.keys_control()  # задействовали управление клавишами
        self.mouse_control()  # задействовали управление мышкой
        self.rect.center = self.x, self.y  # туда уже перемещаем центр квадрата (нашего игрока)
        self.angle %= DOUBLE_PI  # угол направления игрока теперь в пределах 2п

    """Подключение клавиш управления"""
    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # выход из приложения по нажатию Esc
            exit()
        # определяем перемещение игрока на следующий шаг как dx, dy
        if keys[pygame.K_w]:
            dx = PLAYER_SPEED * cos_a  # Нахождение точки по направлению луча
            dy = PLAYER_SPEED * sin_a
            self.detect_collision(dx, dy)  # вызываем эту ф-ю после нажатия каждой кнопки
        if keys[pygame.K_s]:
            dx = -PLAYER_SPEED * cos_a
            dy = -PLAYER_SPEED * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = PLAYER_SPEED * sin_a
            dy = -PLAYER_SPEED * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -PLAYER_SPEED * sin_a
            dy = PLAYER_SPEED * cos_a
            self.detect_collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

        # после выстрела идет анимация перезарядки.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.shot:
                    self.shot = True

    """Управление мышью"""
    def mouse_control(self):
        if pygame.mouse.get_focused():  # когда курсор в окне игры, мы
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH  # разница = положение текущ. х мышки - середина экрана
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))  # с каждым циклом переносим указатель мышки в центр экрана
            # и прибавлять разницу к углу направления игрока с учетом чувствительности мыши:
            self.angle += difference * self.sensitivity
