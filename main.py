import pygame
from sys import exit
from random import randint
import time

def display_score():
   time = int(pygame.time.get_ticks() / 800) - start_time
   score_surf = text_font.render(f'{time}', False, 'Blue')
   score_rect = score_surf.get_rect(center = (400, 60))
   screen.blit(score_surf, score_rect)
   return time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 360:
                screen.blit(enemya_surf, obstacle_rect)
            else: 
                screen.blit(enemyb_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return [ ]

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True
         
pygame.init()
screen =  pygame.display.set_mode((800,400))
screen_rect = screen.get_rect(x = 0)
pygame.display.set_caption('Forrest Gump')
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0

#Obstacles
enemya_surf = pygame.image.load('enemy.png').convert_alpha()
enemya_surf = pygame.transform.scale(enemya_surf, (50,50))

enemyb_surf = pygame.image.load('enemyb.png').convert_alpha()
enemyb_surf = pygame.transform.scale(enemyb_surf, (70,70))

obstacle_rect_list =[ ]


sky_surf = pygame.image.load('screen1.jpg').convert_alpha()
sky_surf = pygame.transform.scale(sky_surf, (800,800))
sky_rect = sky_surf.get_rect(x = 0)

ground_surf = pygame.image.load('ground.jpg').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf, (800,100))
sky_rect = ground_surf.get_rect(y = 0)

text_font = pygame.font.SysFont('Ariel', 55)
name_surf = text_font.render('Forrest Gump', False, (0,0,2))
name_rect = name_surf.get_rect(center = (400,20))

player_surf = pygame.image.load('char.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (80,80))
player_rect = player_surf.get_rect(bottomleft = (100,360))

restart_surf = pygame.image.load('screen2.jpg').convert_alpha()
restart_surf = pygame.transform.scale(restart_surf, (800, 800))
restart_rect = restart_surf.get_rect(x = 0)

pic_player_surf = pygame.image.load('char.png').convert_alpha()
pic_player_surf = pygame.transform.scale(pic_player_surf, (190,190))
pic_player_rect = pic_player_surf.get_rect(center = (400,98))

over_font = pygame.font.SysFont('Ariel', 100)
over_surf = over_font.render('Game over', False, 'Red')
over_rect = over_surf.get_rect(center = (400, 195))

start_font = pygame.font.SysFont('Ariel', 30)
start_surf = start_font.render('Press the character to start', False, 'Blue')
start_rect = start_surf.get_rect(center = (400, 195))

player_gravity = 0

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and  player_rect.bottom >= 180:
                    player_gravity = -18

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 180:
                    player_gravity = -18
                if event.key == pygame.K_LEFT and player_rect.left >= 0:
                    player_rect.left -= 5
                if event.key == pygame.K_RIGHT and player_rect.right <= 300:
                    player_rect.right += 5

            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(enemya_surf.get_rect(bottomleft = (randint(850, 1500) ,360)))
                else:
                    obstacle_rect_list.append(enemyb_surf.get_rect(bottomleft = (randint(850, 1500) ,280)))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 800)

            elif event.type == pygame.MOUSEBUTTONDOWN and pic_player_rect.collidepoint(event.pos):
                game_active = True
                start_time = int(pygame.time.get_ticks() / 800)

    if game_active:
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))
        # screen.blit(name_surf, name_rect)
        score = display_score()


        # enemya_rect.right -= 5
        # if enemya_rect.right <= 0: enemya_rect.left =800
        # screen.blit(enemya_surf,enemya_rect)

        #Player
        player_gravity += 0.8
        player_rect.y += player_gravity
        if player_rect.bottom >= 360:
            player_rect.bottom = 360
        screen.blit(player_surf, player_rect)

        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #Collision
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.blit(restart_surf, restart_rect)
        screen.blit(name_surf, name_rect)
        screen.blit(pic_player_surf, pic_player_rect)
        obstacle_rect_list.clear()
        player_rect.bottomleft = (100,360)
        player_gravity = 0
        
        over_score =text_font.render(f'Your score: {score}', False, (34,0,150))
        over_score_rect = over_score.get_rect(center = (400, 250))

        if score == 0:
            screen.blit(start_surf, start_rect)
        else:
            screen.blit(over_surf, over_rect)
            screen.blit(over_score, over_score_rect)

    pygame.display.update()
    clock.tick(60)