import pygame
from settings import *
from map import mini_map
from collections import deque
from random import randrange
import sys


class Drawing:
    def __init__(self, sc, sc_map, player, clock):  # (экземпляр класса игрок)
        self.sc = sc  # поверхность для карты
        self.sc_map = sc_map  # поверхность для уменьшенной карты
        self.player = player
        self.clock = clock
        # Кол-во кадров в игре, как в обычных играх. Для этого определяем новый атрибут системного шрифта:
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.font_win = pygame.font.Font('font/font.ttf', 144)
        self.textures = {1: pygame.image.load('img/wall3.png').convert(),
                         2: pygame.image.load('img/wall4.png').convert(),
                         3: pygame.image.load('img/wall5.png').convert(),
                         4: pygame.image.load('img/wall6.png').convert(),
                         'S': pygame.image.load('img/sky2.png').convert(),
                         }  # ключи - номера стен, значения - текстуры

        # menu
        self.menu_trigger = True  # триггер меню
        self.menu_picture = pygame.image.load('img/bg.jpg').convert()  # картинка для фона

        # weapon parameters
        self.weapon_base_sprite = pygame.image.load('sprites/weapons/shotgun/base/0.png').convert_alpha()
        self.weapon_shot_animation = deque([pygame.image.load(f'sprites/weapons/shotgun/shot/{i}.png').convert_alpha()
                                            for i in range(20)])
        self.weapon_rect = self.weapon_base_sprite.get_rect()
        self.weapon_pos = (HALF_WIDTH - self.weapon_rect.width // 2, HEIGHT - self.weapon_rect.height)
        self.shot_projection = 0
        self.shot_length = len(self.weapon_shot_animation)
        self.shot_length_count = 0
        self.shot_animation_speed = 3
        self.shot_animation_count = 0
        self.shot_animation_trigger = True
        self.shot_sound = pygame.mixer.Sound('sound/shotgun.wav')  # звук выстрела для оружия

        # sfx parameters
        self.sfx = deque([pygame.image.load(f'sprites/weapons/sfx/{i}.png').convert_alpha() for i in range(9)])
        self.sfx_length_count = 0
        self.sfx_length = len(self.sfx)

    # Фон игры, принимает в параметр угол игрока, Реализация динамического неба
    def background(self, angle):
        # смещение по текстуре путем нахождения остатка от деления обратного направления игрока на ширину главного окна:
        sky_offset = -10 * math.degrees(angle) % WIDTH
        # нарисуем три участка неба в зависимости от смещения, чтобы не было видно пробелов
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARK_GRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    # Главная проекция
    def world(self, world_objects):
        # сортируем стены и спрайты по глубине (алгоритм зет-буфера)
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, obj, object_pos = obj  # отсекаем ложные значения для спрайтов, распаковываем кортеж
                self.sc.blit(obj, object_pos)  # наносим объекты на главную поверхность

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))  # поможет получить инфу о кол-ве кадров в секунду
        render = self.font.render(display_fps, False, DARK_ORANGE)  # определим цвет
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
            pygame.draw.rect(self.sc_map, DARK_BROWN, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)  # мини-карта в левом нижнем углу главной поверхности

    def player_weapon(self, shots):
        # в зависимости от параметра нажатой клавиши мыши, будем проигрывать спрайты с установленной скоростью анимации
        if self.player.shot:
            if not self.shot_length_count:  # в момент старта анимации выстрела
                self.shot_sound.play()  # включается звук выстрела
            self.shot_projection = min(shots)[1] // 2  # кто ближе: стена или спрайт, взяв минимум по расстоянию от них
            self.bullet_sfx()
            shot_sprite = self.weapon_shot_animation[0]
            self.sc.blit(shot_sprite, self.weapon_pos)
            self.shot_animation_count += 1
            if self.shot_animation_count == self.shot_animation_speed:
                self.weapon_shot_animation.rotate(-1)
                self.shot_animation_count = 0
                self.shot_length_count += 1
                self.shot_animation_trigger = False
            if self.shot_length_count == self.shot_length:
                self.player.shot = False
                self.shot_length_count = 0
                self.sfx_length_count = 0
                self.shot_animation_trigger = True
        else:  # если спрайты закончатся, будем присваивать атрибуту ложное значение
            self.sc.blit(self.weapon_base_sprite, self.weapon_pos)

    # эффект от разрыва пули:
    def bullet_sfx(self):
        """Тот эе механизм для реализации анимации, в котором будем масштабировать по проекционной высоте
        спрайтовые картинки, тем самым будем получать эффект пули по ближайшему объекту"""
        if self.sfx_length_count < self.sfx_length:
            sfx = pygame.transform.scale(self.sfx[0], (self.shot_projection, self.shot_projection))
            sfx_rect = sfx.get_rect()
            self.sc.blit(sfx, (HALF_WIDTH - sfx_rect.w // 2, HALF_HEIGHT - sfx_rect.h // 2))
            self.sfx_length_count += 1
            self.sfx.rotate(-1)

    # Поздравление победителя
    def win(self):
        render = self.font_win.render('YOU WIN!!!', True, (randrange(40, 120), 0, 0))  # Надпись рандомно меняет цвет
        rect = pygame.Rect(0, 0, 1000, 300)  #
        rect.center = HALF_WIDTH, HALF_HEIGHT
        pygame.draw.rect(self.sc, BLACK, rect, border_radius=50)  # черный прямоугольник с круглыми краями
        self.sc.blit(render, (rect.centerx - 430, rect.centery - 80))
        pygame.display.flip()
        self.clock.tick(15)

    def menu(self):
        x = 0
        button_font = pygame.font.Font('font/font.ttf', 72)  # шрифт для кнопок
        label_font = pygame.font.Font('font/font1.otf', 400)  # шрифт для названия игры
        start = button_font.render('START', True, pygame.Color('lightgray'))  # надпись для первой кнопки
        button_start = pygame.Rect(0, 0, 400, 150)  # прямоугольник для первой кнопки
        button_start.center = HALF_WIDTH, HALF_HEIGHT  # кнопка по центру
        exit_game = button_font.render('EXIT', True, pygame.Color('lightgray'))  # надпись для второй кнопки
        button_exit = pygame.Rect(0, 0, 400, 150)  # прямоугольник для второй кнопки
        button_exit.center = HALF_WIDTH, HALF_HEIGHT + 200  # кнопка ниже центра на 200

        while self.menu_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.sc.blit(self.menu_picture, (0, 0), (x % WIDTH, HALF_HEIGHT, WIDTH, HEIGHT))
            x += 1  # на фоне по координате х будет медленно перемещаться картинка

            pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25, width=10)
            self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 40))
            # (.., цвет краев, .., .., уровень закрашенности)
            pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25, width=10)
            self.sc.blit(exit_game, (button_exit.centerx - 85, button_exit.centery - 40))

            color = randrange(40)  # надпись игры рандомно будем менять в сером диапазоне
            label = label_font.render('DOOMPy', True, (color, color, color))  # надпись игры
            self.sc.blit(label, (15, -30))

            mouse_pos = pygame.mouse.get_pos()  # получаем координаты мыши
            mouse_click = pygame.mouse.get_pressed()  # и состояние нажатых клавиш мыши
            if button_start.collidepoint(mouse_pos):  # если мышка оказывается над кнопкой
                # то кнопка рисуется так же, но фон становится полностью закрашен
                pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25)
                self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))
                if mouse_click[0]:  # в зависимости от нажатой кнопки по щелчку
                    self.menu_trigger = False  # или запускаем главный цикл (игру)
            elif button_exit.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25)
                self.sc.blit(exit_game, (button_exit.centerx - 85, button_exit.centery - 70))
                if mouse_click[0]:
                    pygame.quit()
                    sys.exit()  # или завершаем работу приложения

            pygame.display.flip()
            self.clock.tick(20)  # экземпляр Клок для установки кол-ва кадров в секунду
