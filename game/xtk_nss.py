import pygame 

white = (255,255,255)
red = (255, 0, 0)
black = (0,0,0)
display_width = int(1280/1)
display_heigth = int(720/1)

class player:
	def __init__(self):
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
        if self.move_right == True:
            self.pos_x += self.speed
        if self.move_left == True:
            self.pos_x -= self.speed
        if self.move_up == True:
        	old_jump_speed = self.jump_speed
        	self.pos_y += self.jump_speed        	 
         	self.jump_speed == self.jump_speed /1.2
        if self.move_up ==False and pos_y < 0:
        	self.jump_speed = old_jump_speed
        	self.pos_y - old_jump_speed
        





