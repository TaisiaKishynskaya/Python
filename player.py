from settings import *
import pygame
import math

"""Для управления игроком"""


class Player:
    def __init__(self):
        self.x, self.y = player_pos  # координаты игрока
        self.angle = player_angle  # направление взгляда

    @property
    def pos(self):
        return self.x, self.y  # вернет позицию по х и у

    """Мы - круг. У нас есть направление луча под углом а. Для каждой клавиши у нас перемещение d должно быть одинаково.
    Все направления отличаются на 90 градусов -> Применяем формулы приведения тригонометрических ф-й для того, чтобы
    найти создать управление подобное 3д, а не 2д."""
    # будет отслеживать нажатые клавиши и менять соответствующее значение атрибутов
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
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

        self.angle %= DOUBLE_PI  # угол направления игрока теперь в пределах 2п
