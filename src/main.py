import pygame
import constants as const
import player as p

# Initialize the game
pygame.init()

# create the screen

screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

#Title and Icon
pygame.display.set_caption(const.TITLE)
pygame.display.set_icon(const.ICON)


# Game loop
all_sprites = pygame.sprite.Group()
player = p.Player()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed_keys = pygame.key.get_pressed()

    screen.fill((255,255,255))

    screen.blit(player.image, (const.SCREEN_WIDTH/2, const.SCREEN_HEIGHT/2))

    all_sprites.update()
    pygame.display.update()