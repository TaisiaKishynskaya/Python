import math

# game settings
WIDTH = 1200  # разрешение экрана
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PENTA_HEIGHT = 5 * HEIGHT  # оптимизация для проекционной высоты
DOUBLE_HEIGHT = 2 * HEIGHT
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)

# minimap settings
MINIMAP_SCALE = 5  # масштабирующий коефициент для карты, чтобы уменьшить нашу карту в 5 раз
MINIMAP_RES = (WIDTH // MINIMAP_SCALE, HEIGHT // MINIMAP_SCALE)  # числ.коеф.,чтобы весь мир отображался в мини-карте
MAP_SCALE = 2 * MINIMAP_SCALE  # 1 -> 12 x 8, 2 -> 24 x 16, 3 -> 36 x 24
MAP_TILE = TILE // MAP_SCALE  # масштабирующий коефициент для стороны квадрата
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

# ray casting settings
FOV = math.pi / 3  # обл. видимости - угол, в который будет попадать всё, что мы видим
HALF_FOV = FOV / 2  # под каким углом будут исходить первый и крайний лучи
NUM_RAYS = 300  # в этой области будем испускать лучи, это их кол-во (не равно WIDTH, т.к. возникнут тормоза в пайтоне)
MAX_DEPTH = 800  # дальность прорисовки - макс. расстояние, на которое будем излучать лучи
DELTA_ANGLE = FOV / NUM_RAYS  # угол между лучами
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))  # расстоние от игрока до экрана
PROJ_COEFF = 3 * DIST * TILE  # проекционный параметр (скорректированный из DIST * TILE, чтобы стена не была растянута)
SCALE = WIDTH // NUM_RAYS  # масштабирующий коэф.

# sprite settings
DOUBLE_PI = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 - 1  # номер центрального луча
FAKE_RAYS = 100  # фейковые лучи
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# texture settings (1200 x 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE  # масштабирующий коеф., чтобы текстура полностью влезла в размер квадрата карты

# player settings
player_pos = (HALF_WIDTH // 4, HALF_HEIGHT - 50)  # позиция игрока
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
SANDY = (244, 164, 96)
DARKBROWN = (97, 61, 25)
DARKORANGE = (255, 140, 0)
