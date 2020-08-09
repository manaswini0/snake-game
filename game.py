import pygame
import random

import snake_class
import obs_class

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Snake-game")

all_sprites = pygame.sprite.Group()
snake = snake_class.Snake(50, 50)
all_sprites.add(snake)
#obstacles
def obstacles():

    for i in range(0,20):
        obs=obs_class.Obs(random.randrange(500),random.randrange(500))
        all_sprites.add(obs)


obstacles()

run = True


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    all_sprites.update()

    win.fill((0,0,0))
    #draws all the sprites on screen
    all_sprites.draw(win)
    pygame.time.delay(25)
    pygame.display.update()


pygame.quit()