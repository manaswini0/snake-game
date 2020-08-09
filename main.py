import pygame
import random
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Snake-game")


vel=5


#making obstacles


class Snake:
    x=50
    y=50
    height=20
    width=25
class Obs():
    x_obs=[]
    y_obs=[]
    h_obs=30
    w_obs=35
obs=Obs()
def obstacles():

    for i in range(0,20):
        obs.x_obs.append(random.randrange(500))
        obs.y_obs.append(random.randrange(500))

#collisons
def collisions(s_s,o_obs):
    if pygame.sprite.collide_rect_ratio(0.5)(s_s,o_obs):
        pygame.draw.rect(win,(255,0,0),(s_s.x,s_s.y,(s_s.height+10),(s_s.width+10)))
        print("jj")


run = True

s = Snake()

obstacles()


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.time.delay(25)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        s.x -= vel
        collisions(s.x,s.y)
    if keys[pygame.K_RIGHT]:
        s.x += vel
        collisions(s.x,s.y)
    if keys[pygame.K_DOWN]:
        s.y += vel
        collisions(s.x,s.y)
    if keys[pygame.K_UP]:
        s.y -= vel
        collisions(s.x,s.y)
    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(s.x,s.y,s.height,s.width))
    for i in range(len(obs.x_obs)):
        pygame.draw.rect(win,(255,255,255),(obs.x_obs[i],obs.y_obs[i],obs.h_obs,obs.w_obs))

    pygame.display.update()

pygame.quit()




