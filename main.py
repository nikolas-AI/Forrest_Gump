import pygame
from sys import exit

pygame.init()
screen =  pygame.display.set_mode((800,400))
pygame.display.set_caption('Forrest Gump')
clock = pygame.time.Clock()


enemy_surf = pygame.image.load('aliena.png')
enemy_surf = pygame.transform.scale(enemy_surf, (70,70))
enemy_rect = enemy_surf.get_rect(bottomleft = (700,300))
x_pos = 700


sky_surf = pygame.Surface((800,300))
sky_surf.fill('skyblue')

ground_surf = pygame.Surface((800,100))
ground_surf.fill('green')

text_font = pygame.font.SysFont('Calbiri', 30)
score_surf = text_font.render('Forrest Gump', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

player_surf = pygame.image.load('alienb.png')
player_surf = pygame.transform.scale(player_surf, (70,70))
player_rect = player_surf.get_rect(bottomleft = (100,300))

player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and  player_rect.bottom >= 300:
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and  player_rect.bottom >= 300:
                    player_gravity = -20


    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
    screen.blit(score_surf,score_rect)

    enemy_rect.right -= 5
    if enemy_rect.right <= 0: enemy_rect.left = 800
    screen.blit(enemy_surf,enemy_rect)

    #Player
    player_gravity += 0.8
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300

    screen.blit(player_surf,player_rect)

    pygame.display.update()
    clock.tick(60)