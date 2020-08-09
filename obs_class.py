import pygame


class Obs(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((25,25))
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
