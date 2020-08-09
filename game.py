import pygame
import random
import os
import snake_class
import obs_class

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Snake-game")

h=20
w=30

snake_sprites = pygame.sprite.Group()
obs_sprites=pygame.sprite.Group()
snake = snake_class.Snake(50, 50,h,w)
snake_sprites.add(snake)


#obstacles
def obstacles():

    for i in range(0,20):
        obs=obs_class.Obs(random.randrange(500),random.randrange(500))
        obs_sprites.add(obs)


obstacles()

def collisions():

    for o in pygame.sprite.spritecollide(snake, obs_sprites, 1):

        pygame.sprite.Sprite.remove(o)
        os.system("afplay snakeatt.mp3&")
        # pygame.sprite.Sprite.remove(snake)
        increase_len()
        # h=h+5
        # w=w+5



def increase_len():



    # snake_sprites.add(snake)
    print ("kk")
run = True


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    snake_sprites.update()

    win.fill((0,0,0))
    #draws all the sprites on screen
    snake.update()
    collisions()
    snake_sprites.draw(win)
    obs_sprites.draw(win)
    pygame.time.delay(25)
    pygame.display.update()


pygame.quit()