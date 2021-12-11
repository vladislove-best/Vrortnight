import pygame 
import random

white = (255,255,255)
red = (255, 0, 0)
black = (0,0,0)
display_width = int(1280/1)
display_heigth = int(720/1)
color = black

class player:

    def __init__(self):
        self.color = 0
        self.speed = 5
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.size = 10
        self.pos_x = display_width//2
        self.pos_y = display_heigth//2
        self.jump_speed = 8

    def walk_right(self):
        self.move_right = True
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def walk_left(self):
        self.move_left = True
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def walk_up(self):
        self.move_right = False
        self.move_left = False
        self.move_up = True
        self.move_down = False

    def walk_down(self):
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = True

    def stop(self):
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        try:
            self.color = gameDisplay.get_at((self.pos_x,self.pos_y))
        except:
            self.color = (0,0,0)
        self.pos_y += self.jump_speed
        if self.move_right == True:
            self.pos_x += self.speed
        if self.move_left == True:
            self.pos_x -= self.speed
        if self.move_up == True:
            old_jump_speed = self.jump_speed       
            self.jump_speed == self.jump_speed /1.2
        if self.move_up == False and self.color == black:
            self.jump_speed = 0
        else:
            self.jump_speed = self.jump_speed - 1
        gameDisplay.blit(player1_viwe, (self.pos_x,self.pos_y))
pygame.init()
pygame.font.init()
gameDisplay = pygame.display.set_mode((display_width, display_heigth))
player1 = player()
player1_viwe = pygame.image.load('a0000723242_16.jpg')
player1_viwe = pygame.transform.scale(player1_viwe, (player1.size, player1.size))
running = True
FPS = 30
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        ############################
        if event.type == pygame.K_a:
            player1.walk_left()             
        if event.type == pygame.K_d:
            player1.walk_right()                        
        if event.type == pygame.K_w:
            player1.walk_up()
        else:
            player1.stop()
        # if event.type == pygame.K_s:
        #     player1.action()
        ############################
    player1.update()
    pygame.display.update()
    clock.tick(FPS)




