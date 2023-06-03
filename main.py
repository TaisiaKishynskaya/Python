from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing
from interaction import Interaction

pygame.init()  # гарантирует правильную инициализацию и подготовку библиотеки перед ее использованием
sc = pygame.display.set_mode((WIDTH, HEIGHT))  # разрешение экрана
sc_map = pygame.Surface(MINIMAP_RES)  # карта на отдельной поверхности, уменьшенной в 5 раз

sprites = Sprites()  # экземпляры спрайтов
clock = pygame.time.Clock()  # объект класса Clock для установки кол-ва кадров в секунду
player = Player(sprites)  # для вз-вия коллизии со спрайтами, экземпляр класса спрайтов передадим в экземпляр игрока
drawing = Drawing(sc, sc_map, player, clock)
interaction = Interaction(player, sprites, drawing)

drawing.menu()  # рисуем меню
pygame.mouse.set_visible(False)  # отключим указатель мышки, чтобы не мешался на экране
interaction.play_music()  # включаем музыку

while True:
    player.movement()
    drawing.background(player.angle)
    walls, wall_shot = ray_casting_walls(player, drawing.textures)
    # передадим список параметров стен + список вычисленных параметров спрайтов, структура их идентична стенам
    drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
    drawing.fps(clock)  # на вход принимает экземпляр класса
    drawing.mini_map(player)
    drawing.player_weapon([wall_shot, sprites.sprite_shot])

    interaction.interaction_objects()
    interaction.npc_action()
    interaction.clear_world()
    interaction.check_win()

    pygame.display.flip()
    clock.tick(FPS)  # задержка для нужного ФПС
