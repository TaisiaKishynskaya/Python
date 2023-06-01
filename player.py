from settings import *
import pygame
import math

"""Для управления игроком"""


class Player:
    def __init__(self):
        self.x, self.y = player_pos  # координаты игрока
        self.angle = player_angle  # направление взгляда
        self.sensitivity = 0.004  # чувствительность мышки

    @property
    def pos(self):
        return self.x, self.y  # вернет позицию по х и у

    """Мы - круг. У нас есть направление луча под углом а. Для каждой клавиши у нас перемещение d должно быть одинаково.
    Все направления отличаются на 90 градусов -> Применяем формулы приведения тригонометрических ф-й для того, чтобы
    найти создать управление подобное 3д, а не 2д."""
    # будет отслеживать нажатые клавиши и менять соответствующее значение атрибутов
    def movement(self):
        self.keys_control()  # задействовали управление клавишами
        self.mouse_control()  # задействовали управление мышкой
        self.angle %= DOUBLE_PI  # угол направления игрока теперь в пределах 2п

    """Подключение клавиш управления"""
    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # выход из приложения по нажатию Esc
            exit()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a  # Нахождение точки по направлению луча
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    """Управление мышью"""
    def mouse_control(self):
        # когда курсор в окне игры, мы
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH  # разница = положение текущ. х мышки - середина экрана
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))  # с каждым циклом переносим указатель мышки в центр экрана
            # и прибавлять разницу к углу направления игрока с учетом чувствительности мыши:
            self.angle += difference * self.sensitivity
