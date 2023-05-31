import math

# game settings
WIDTH = 1200  # разрешение экрана
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)

# minimap settings
MAP_SCALE = 5  # масштабирующий коефициент для карты, чтобы уменьшить нашу карту в 5 раз
MAP_TILE = TILE // MAP_SCALE  # масштабирующий коефициент для стороны квадрата
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

# ray casting settings
FOV = math.pi / 3  # обл. видимости - угол, в который будет попадать всё, что мы видим
HALF_FOV = FOV / 2  # под каким углом будут исходить первый и крайний лучи
NUM_RAYS = 300  # в этой области будем испускать лучи, это их кол-во (не равно WIDTH, т.к. возникнут тормоза в пайтоне)
MAX_DEPTH = 800  # дальность прорисовки - макс. расстояние, на которое будем излучать лучи
DELTA_ANGLE = FOV / NUM_RAYS  # угол между лучами
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))  # расстоние от игрока до экрана
PROJ_COEFF = 3 * DIST * TILE  # проекционный параметр (скорректированный из PROJ_COEFF = DIST * TILE)
SCALE = WIDTH // NUM_RAYS  # масштабирующий коэф.

# player settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)  # позиция игрока
player_angle = 0  # направление взгляда
player_speed = 2  # скорость передвижения

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
