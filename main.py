import pygame
from sys import exit

def display_score():
   time = int(pygame.time.get_ticks() / 800) - start_time
   score_surf = text_font.render(f'{time}', False, 'Blue')
   score_rect = score_surf.get_rect(center = (400, 60))
   screen.blit(score_surf, score_rect)

pygame.init()
screen =  pygame.display.set_mode((800,400))
screen_rect = screen.get_rect(x = 0)
pygame.display.set_caption('Forrest Gump')
clock = pygame.time.Clock()
game_active = True
start_time = 0

enemy_surf = pygame.image.load('enemy.png').convert_alpha()
enemy_surf = pygame.transform.scale(enemy_surf, (70,70))
enemy_rect = enemy_surf.get_rect(bottomleft = (700,350))
x_pos = 700


# sky_surf = pygame.Surface((800,300))
# sky_surf.fill('skyblue')

sky_surf = pygame.image.load('screen1.jpg').convert_alpha()
sky_surf = pygame.transform.scale(sky_surf, (800,800))
sky_rect = sky_surf.get_rect(x = 0)

ground_surf = pygame.image.load('ground.jpg').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf, (800,100))
sky_rect = ground_surf.get_rect(y = 0)

# ground_surf = pygame.Surface((800,100))
# ground_surf.fill('green')

text_font = pygame.font.SysFont('Ariel', 40)
name_surf = text_font.render('Forrest Gump', False, 'Black')
name_rect = name_surf.get_rect(center = (400,20))

player_surf = pygame.image.load('chara.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (70,70))
player_rect = player_surf.get_rect(bottomleft = (100,320))

restart_surf = pygame.image.load('screen2.jpg').convert_alpha()
restart_surf = pygame.transform.scale(restart_surf, (800, 800))
restart_rect = restart_surf.get_rect(x = 0)

pic_player_surf = pygame.image.load('chara.png').convert_alpha()
pic_player_surf = pygame.transform.scale(pic_player_surf, (100,100))
pic_player_rect = pic_player_surf.get_rect(center = (400,90))

over_font = pygame.font.SysFont('Ariel', 100)
over_surf = over_font.render('Game over', False, 'Red')
over_rect = over_surf.get_rect(center = (400, 170))

over_score =text_font.render(f'Your score: {int(pygame.time.get_ticks() / 800)}', False, 'Blue')
over_score_rect = over_score.get_rect(center = (400, 230))

start_font = pygame.font.SysFont('Ariel', 60)
start_surf = start_font.render('Press to continue: ', False, 'Red')
start_rect = start_surf.get_rect(center = (300, 140))


player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and  player_rect.bottom >= 260:
                    player_gravity = -18

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 260:
                    player_gravity = -18
                if event.key == pygame.K_LEFT and player_rect.left >= 0:
                    player_rect.left -= 5
                if event.key == pygame.K_RIGHT and player_rect.right <= 300:
                    player_rect.right += 5
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 800)

            elif event.type == pygame.MOUSEBUTTONDOWN and pic_player_rect.collidepoint(event.pos):
                game_active = True
                enemy_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 800)


    if game_active:
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))
        # pygame.draw.rect(screen, '#c0e8ec',score_rect)
        # pygame.draw.rect(screen, '#c0e8ec',score_rect,10)
        screen.blit(name_surf, name_rect)
        display_score()


        enemy_rect.right -= 5
        if enemy_rect.right <= 0: enemy_rect.left =800
        screen.blit(enemy_surf,enemy_rect)

        #Player
        player_gravity += 0.8
        player_rect.y += player_gravity
        if player_rect.bottom >= 350:
            player_rect.bottom = 350
        screen.blit(player_surf, player_rect)

        #Collision
        if enemy_rect.colliderect(player_rect):
            game_active = False
            player_rect.left = 100

    else:
        screen.blit(restart_surf, restart_rect)
        screen.blit(name_surf, name_rect)
        screen.blit(over_surf, over_rect)
        screen.blit(over_score, over_score_rect)
        screen.blit(pic_player_surf, pic_player_rect)

    pygame.display.update()
    clock.tick(60)