import pygame
from sys import exit

pygame.init()
screen =  pygame.display.set_mode((800,400))
pygame.display.set_caption('Forrest Gump')
clock = pygame.time.Clock()


enemy_surf = pygame.Surface((20,20))
enemy_surf.fill('red')
enemy_rect = enemy_surf.get_rect(bottomleft = (700,300))
x_pos = 700

sky_surf = pygame.Surface((800,300))
sky_surf.fill('skyblue')

ground_surf = pygame.Surface((800,100))
ground_surf.fill('green')

text_font = pygame.font.SysFont('Calbiri', 30)
score_surf = text_font.render('Forrest Gump', False, 'Black')
score_rect = score_surf.get_rect(center = (400,50))

player_surf = pygame.Surface((20,20))
player_surf.fill('white')
player_rect = player_surf.get_rect(bottomleft = (100,300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('collision')

    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    screen.blit(score_surf,score_rect)

    enemy_rect.right -= 2
    if enemy_rect.right <= 0: enemy_rect.left = 800
    screen.blit(enemy_surf,enemy_rect)

    player_rect.left += 1
    screen.blit(player_surf,player_rect)

    # if player_rect.colliderect(enemy_rect):
    #     print("collision")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())
    

    pygame.display.update()
    clock.tick(60)