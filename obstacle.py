import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            enemy_surf = pygame.image.load('enemyb.png').convert_alpha()
            enemy_surf = pygame.transform.scale(enemy_surf, (60,60))
            self.image = enemy_surf
            self.rect = enemy_surf.get_rect(bottomleft = (randint(850, 1500) ,280))
        else:
            enemy_surf = pygame.image.load('enemy.png').convert_alpha()
            enemy_surf = pygame.transform.scale(enemy_surf, (50,50))
            self.image = enemy_surf
            self.rect = enemy_surf.get_rect(bottomleft = (randint(850, 1500) ,360))


    def update(self):
        self.rect.x -= 5
        self.destroy()

    def destroy(self):
        if self.rect.x <= -50:
            self.kill()
