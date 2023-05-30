import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('char.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(bottomleft = (130,360))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 180:
            self.gravity = -18

    def apply_gravity(self):
        self.gravity += 0.8
        self.rect.y += self.gravity
        if self.rect.bottom >= 360:
            self.rect.bottom = 360
    
    def update(self):
        self.player_input()
        self.apply_gravity()