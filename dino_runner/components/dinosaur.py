import pygame

from dino_runner.utils.constants import DUCKING_HAMMER, DUCKING_SHIELD, HAMMER, HAMMER_TYPE, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING, DUCKING, JUMPING, JUMP_SOUND, DEFAULT_TYPE, RUNNING_HAMMER, SCREEN_HEIGHT, SHIELD_TYPE, RUNNING_SHIELD, THROWN_HAMMER
from dino_runner.components.power_ups.thrown_object import Thrown_Object

class Dinosaur():
    Y_POS = 310
    X_POS = 80
    Y_POS_DUCK = 340
    Y_JUMP_SPEED = 8.5

    def __init__(self):
        self.image = RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index = 0

        self.running = True
        self.ducking = False
        self.jumping = False

        self.jump_speed = self.Y_JUMP_SPEED
        
        self.type = DEFAULT_TYPE
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER }
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER }
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER }
        self.power_up_time = 0
        self.hammer = []

        self.lifes = 1
        
        self.jump_sound = pygame.mixer.Sound(JUMP_SOUND)
        self.thrown_hammer = pygame.mixer.Sound(THROWN_HAMMER)

    def update(self, user_input):
        if self.running:
            self.run()
        if self.ducking:
            self.duck()
        if self.jumping:
            self.jump(user_input)
        
        if user_input[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 13
        if user_input[pygame.K_RIGHT] and self.rect.x < 1015:
            if user_input[pygame.K_LEFT]:
                self.rect.x += 3
            self.rect.x += 10

        if user_input[pygame.K_DOWN] and not self.jumping:
            self.running = False
            self.ducking = True
            self.jumping = False
        elif user_input[pygame.K_UP] or user_input[pygame.K_SPACE] and not self.jumping:
            if not self.jumping:
                self.jump_sound.play()

            self.running = False
            self.ducking = False
            self.jumping = True
        elif not (self.jumping or user_input[pygame.K_DOWN]):
            self.running = True
            self.ducking = False
            self.jumping = False
        
        if user_input[pygame.K_e]:
            if self.type == HAMMER_TYPE:
                self.type = DEFAULT_TYPE
                self.power_up_time = 0
                self.thrown_hammer.play()
                self.hammer.append(Thrown_Object(HAMMER, self.rect.x, self.rect.y))

        self.step_index += 1
        if self.step_index > 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for hammer in self.hammer:
            hammer.update()
            hammer.draw(screen)
            if hammer.rect.x > SCREEN_HEIGHT * 2:
                self.hammer.pop(0)

    def run(self):
        if self.step_index > 5:
            self.image = self.run_img[self.type][0]
        else:
            self.image = self.run_img[self.type][1]
        self.rect.y = self.Y_POS

    def duck(self):
        if self.step_index > 5:
            self.image = self.duck_img[self.type][0]
        else:
            self.image = self.duck_img[self.type][1]
        self.rect.y = self.Y_POS_DUCK

    def jump(self, user_input):
        self.image = self.jump_img[self.type]
        if self.jumping:
            self.rect.y -= self.jump_speed * 4
            self.jump_speed -= 0.8
        if self.jump_speed <- self.Y_JUMP_SPEED: 
            self.jumping = False
            self.rect.y = self.Y_POS
            self.jump_speed = self.Y_JUMP_SPEED
        if user_input[pygame.K_DOWN]:
            self.jump_speed -= 0.6
    
    def move_to_origin_pos(self):
        self.image = RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index = 0

        self.running = True
        self.ducking = False
        self.jumping = False

        self.jump_speed = self.Y_JUMP_SPEED

        self.type = DEFAULT_TYPE

    def activate_power_up(self, power_up_type):
        self.type = power_up_type
        
        