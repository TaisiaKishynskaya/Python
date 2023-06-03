import pygame
from settings import *
from player import Player
from sprite_objects import *
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))  # разрешение экрана
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))  # карта на отдельной поверхности, уменьшеной в 5 раз

sprites = Sprites()  # экземпляры спрайтов
clock = pygame.time.Clock()  # объект класса Clock для установки кол-ва кадров в секунду
player = Player()
drawing = Drawing(sc, sc_map)

while True:
    for event in pygame.event.get():  # проверим все события
        if event.type == pygame.QUIT:  # на предмет закрытия окна и выхода из приложения
            exit()
    player.movement()
    sc.fill(BLACK)

    drawing.background(player.angle)
    walls = ray_casting(player, drawing.textures)
    # передадим список параметров стен + список вычесленых параметров спрайтов, структура их идентична стенам
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    drawing.fps(clock)  # на вход принимает экземпляр класса
    # drawing.mini_map(player)

    pygame.display.flip()
    clock.tick()  # задержка для нужного ФПС
