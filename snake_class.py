import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((20,50))
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
