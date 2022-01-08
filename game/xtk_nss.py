import pygame 
import random

stages_library =[]
white = (255,255,255)
red = (255, 0, 0)
black = (0,0,0)
display_width = int(1280)
display_heigth = int(720)
background = pygame.image.load('spring_bg.png')
class player:
    def __init__(self):
        self.color = 0
        self.color2 = 0
        self.speed = 5
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.size = 10
        self.pos_x = display_width//2
        self.pos_y = 650
        self.jump_speed = 0

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
            self.color = gameDisplay.get_at((int(self.pos_x + self.size/2), int(self.pos_y + self.size)))
            self.color2 = gameDisplay.get_at((int(self.pos_x + self.size/2), int(self.pos_y + 1.5 * self.size)))
        except:
            self.color = black
        # print(self.color)
        if self.move_right == True:
            self.pos_x += self.speed
        if self.move_left == True:
            self.pos_x -= self.speed
        if self.move_up == True:    
            self.jump_speed = 8
            self.pos_y -= 15
            self.move_up = False  
        elif self.move_up == False and sum(self.color) < 450 or sum(self.color2) < 450:
            self.jump_speed = 0
            print('чёрный под мной')
        else:
            self.jump_speed = self.jump_speed - 1
        print(self.pos_y)
        print(self.color)
        print(self.move_up)
        self.pos_y -= self.jump_speed
        if self.pos_y>0.98*display_heigth:
            exit()
        gameDisplay.blit(player1_viwe, (self.pos_x,self.pos_y))
pygame.init()
pygame.font.init()
gameDisplay = pygame.display.set_mode((display_width, display_heigth))
player1 = player()
player1_viwe = pygame.image.load('a0000723242_16.jpg')
player1_viwe = pygame.transform.scale(player1_viwe, (player1.size, player1.size))
running = True
FPS = 60
clock = pygame.time.Clock()
for i in range (4):
    stages_library.append(pygame.image.load('stage('+str(random.randint(1,1))+').bmp'))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1.walk_left()             
            if event.key == pygame.K_d:
                player1.walk_right()                        
            if event.key == pygame.K_w:
                player1.walk_up()
                print('srv')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player1.stop()
        # if event.type == pygame.K_s:
        #     player1.action()
        ############################
    gameDisplay.blit(background, (0,0))
    for i in range (len(stages_library)):
        gameDisplay.blit(stages_library[i], (910,520 - (160 * i)))
    player1.update()
    pygame.display.update()
    clock.tick(FPS)