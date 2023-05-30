import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            enemyb_surf = pygame.image.load('enemyb.png').convert_alpha()
            enemyb_surf = pygame.transform.scale(enemyb_surf, (60,60))
            y_pos = 280
        else:
            enemya_surf = pygame.image.load('enemy.png').convert_alpha()
            enemya_surf = pygame.transform.scale(enemya_surf, (50,50))
            y_pos = 360
        self.images
        self.rect