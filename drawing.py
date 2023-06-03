import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc  # поверхность для карты
        self.sc_map = sc_map  # поверхность для уменьшенной карты
        self.font = pygame.font.SysFont('Arial', 36, bold=True)  # кол-во кадров в игре, как в обычных играх
        # для этого определяем новый атрибут системного шрифта и

    # Фон игры
    def background(self):
        pygame.draw.rect(self.sc, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    # Главная проекция
    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle)

    #
    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))  # поможет получить инфу о кол-ве кадров в секунду
        render = self.font.render(display_fps, 0, RED)  # определим цвет
        self.sc.blit(render, FPS_POS)  # и разместим его в правом верхнем углу нашего окна

    # Вывод мини-карты
    def mini_map(self, player):
        self.sc_map.fill(BLACK)  # цвет поверхности черный
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE  # позицию игрока масштабируем, уменьшая в 5 раз
        # Выведем элементы мини-карты на её отдельную поверхность:
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                               map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, GREEN, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)  # мини-карта в левом нижнем углу главной поверхности
