import pygame
from settings import *
from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))  # разрешение экрана
pygame.mouse.set_visible(False)  # отключим указатель мышки, чтобы не мешался на экране
sc_map = pygame.Surface(MINIMAP_RES)  # карта на отдельной поверхности, уменьшенной в 5 раз

sprites = Sprites()  # экземпляры спрайтов
clock = pygame.time.Clock()  # объект класса Clock для установки кол-ва кадров в секунду
player = Player(sprites)  # для вз-вия коллизии со спрайтами, экземпляр класса спрайтов передадим в экземпляр игрока
drawing = Drawing(sc, sc_map)

while True:
    for event in pygame.event.get():  # проверим все события
        if event.type == pygame.QUIT:  # на предмет закрытия окна и выхода из приложения
            exit()
    player.movement()
    sc.fill(BLACK)

    drawing.background(player.angle)
    walls = ray_casting_walls(player, drawing.textures)
    # передадим список параметров стен + список вычисленных параметров спрайтов, структура их идентична стенам
    drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
    drawing.fps(clock)  # на вход принимает экземпляр класса
    drawing.mini_map(player)

    pygame.display.flip()
    clock.tick(FPS)  # задержка для нужного ФПС
