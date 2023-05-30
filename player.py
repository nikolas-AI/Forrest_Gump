import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/char.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(bottomleft = (130,360))
        self.gravity = 0

        # self.jump_sound = pygame.mixer.Sound('jump.mp3')
        # self.jump_sound.set_volume(0.5)


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 200:
            self.gravity = -15
            # self.jump_sound.play()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
                self.rect.left -= 5
        if keys[pygame.K_RIGHT] and self.rect.right <= 300:
                self.rect.right += 5

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 360:
            self.rect.bottom = 360
    
    def update(self):
        self.player_input()
        self.apply_gravity()