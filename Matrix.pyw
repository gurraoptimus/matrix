import os 
import pygame as pg
from randomm import choice, randrange


class Symbol:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.value = choice(green_katakana)

        def draw(self):
            surface.blit(self.value,(self.x, self.y))
os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 400, 600
FONT_SIZE = 40

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()

katakana =[chr(int('0x30a0', 16) + i)for i in range(96)]
font = pg.font.SysFont('ms mincho',FONT_SIZE, bold=True)
green_katakana = [font.render(char, True, pg.Color('green')) for char in katakana]

while True:
    surface.fill(pg.Color('black'))

    [exit() for i in pg.event.get()if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60)