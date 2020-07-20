import pygame
import constants as const

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (const.SCREEN_WIDTH / 2, const.SCREEN_HEIGHT / 2)
    
    # def update(self):