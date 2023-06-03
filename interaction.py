from settings import *
from map import world_map
from ray_casting import mapping
import math
import pygame
from numba import njit


@njit(fastmath=True, cache=True)
def ray_casting_npc_player(npc_x, npc_y, blocked_doors, world_map_game, player_person_pos):
    """Задача ф-ии - пускать всего 1 луч. Результат - "находится ли перс в прямой линии видимости с npc?".
    Эта инфа нужна для запуска ф-ии анимации npc при виде игрока - анимация нападения на перса со стороны npc"""
    ox, oy = player_person_pos
    xm, ym = mapping(ox, oy)
    delta_x, delta_y = ox - npc_x, oy - npc_y
    cur_angle = math.atan2(delta_y, delta_x)
    cur_angle += math.pi

    sin_a = math.sin(cur_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = math.cos(cur_angle)
    cos_a = cos_a if cos_a else 0.000001

    # verticals
    x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
    for i in range(0, int(abs(delta_x)) // TILE):
        depth_v = (x - ox) / cos_a
        yv = oy + depth_v * sin_a
        tile_v = mapping(x + dx, yv)
        if tile_v in world_map_game or tile_v in blocked_doors:  # blocked_doors, чтобы npc не видели нас сквозь двери
            return False
        x += dx * TILE

    # horizontals
    y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
    for i in range(0, int(abs(delta_y)) // TILE):
        depth_h = (y - oy) / sin_a
        xh = ox + depth_h * cos_a
        tile_h = mapping(xh, y + dy)
        if tile_h in world_map_game or tile_h in blocked_doors:
            return False
        y += dy * TILE
    return True


class Interaction:
    def __init__(self, player, sprites, drawing):
        self.player = player  # Экземпляр класса Игрок
        self.sprites = sprites  # Экземпляр класса Спрайты
        self.drawing = drawing  # Экземпляр класса Рисование
        self.pain_sound = pygame.mixer.Sound('sound/pain.wav')  # звук криков

    # Ф-я определяет, нах. ли какой-то живой/бессмертный объект в области выстрела
    def interaction_objects(self):
        if self.player.shot and self.drawing.shot_animation_trigger:
            for obj in sorted(self.sprites.list_of_objects, key=lambda object_sprite: object_sprite.distance_to_sprite):
                if obj.is_on_fire[1]:
                    if obj.is_dead != 'immortal' and not obj.is_dead:
                        # если ф-я ray_casting_npc_player выдает True (то есть в момент попадания пули), ...
                        if ray_casting_npc_player(obj.x, obj.y,
                                                  self.sprites.blocked_doors,
                                                  world_map, self.player.pos):
                            if obj.flag == 'npc':  # если наш объект npc, то
                                self.pain_sound.play()  # то запускаем звук криков у этого объекта
                            obj.is_dead = True  # ..то запускаем анимацию смерти у этого объекта
                            obj.blocked = None  # и делаем его проходимым
                            self.drawing.shot_animation_trigger = False
                    # условие открытия дверей - выстрел по ней с расстояния меньше, чем размер клетки
                    if obj.flag in {'door_h', 'door_v'} and obj.distance_to_sprite < TILE:
                        obj.door_open_trigger = True
                        obj.blocked = None
                    break  # обрываем цикл, чтобы не убить одной пулей несколько объектов

    # Ф-я запуска анимации взаимодействия npc
    def npc_action(self):
        # анимация будет запускаться у всех объектов, которые находятся на расстоянии прямой видимости с игроком
        for obj in self.sprites.list_of_objects:
            if obj.flag == 'npc' and not obj.is_dead:
                if ray_casting_npc_player(obj.x, obj.y,
                                          self.sprites.blocked_doors,
                                          world_map, self.player.pos):
                    obj.npc_action_trigger = True
                    self.npc_move(obj)
                else:
                    obj.npc_action_trigger = False

    # Движение npc в нашу сторону
    def npc_move(self, obj):   # Вместо алгоритма поиска пути, делаем проще:
        if abs(obj.distance_to_sprite) > TILE:  # когда расстояние до npc больше размера клетки на карте,
            dx = obj.x - self.player.pos[0]
            dy = obj.y - self.player.pos[1]
            obj.x = obj.x + 1 if dx < 0 else obj.x - 1  # npc двигается в нашу сторону
            obj.y = obj.y + 1 if dy < 0 else obj.y - 1

    # Метод обнаруживает и удаляет открытые двери
    def clear_world(self):
        deleted_objects = self.sprites.list_of_objects[:]
        [self.sprites.list_of_objects.remove(obj) for obj in deleted_objects if obj.delete]

    # Добавление звука
    @staticmethod
    def play_music():
        pygame.mixer.pre_init(44100, -16, 2, 2048)  # инициализируем параметры звукового миксера
        pygame.mixer.init()
        pygame.mixer.music.load('sound/theme.mp3')  # загрузим музыку
        pygame.mixer.music.play(10)  # поставим на воспроизведение

    # Концовка
    def check_win(self):
        # Концовка запускается в тот момент, когда не останется ни одного npc
        if not len([obj for obj in self.sprites.list_of_objects if obj.flag == 'npc' and not obj.is_dead]):
            pygame.mixer.music.stop()  # остановим текущую музыку
            pygame.mixer.music.load('sound/win.mp3')  # загрузим новую
            pygame.mixer.music.play()  # и воспроизведем
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                self.drawing.win()
