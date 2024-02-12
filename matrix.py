import os 
import pygame as pg
# from randomm import choice, randrange

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT =1600, 900
FONT_SIZE = 40

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()

katakana =[chr(int('0x30a0', 16) + i)for i in range(96)]

while True:
    surface.fill(pg.Color('black'))

    [exit() for i in pg.event.get()if i.type == pg.quit]
    pg.display.flip()
    clock.tick(60)