import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.asteroid import Asteroid
from dino_runner.utils.constants import ACTIVATE_ASTEROID, DESTRUCTION, DINO_COLLIDERECT, GAME_OVER_SOUND, PTERODACTILO, SHIELD_TYPE

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []

        self.die = pygame.mixer.Sound(GAME_OVER_SOUND)
        self.dino_colliderect = pygame.mixer.Sound(DINO_COLLIDERECT)
        self.destruction = pygame.mixer.Sound(DESTRUCTION)
        self.activate_asteroid = pygame.mixer.Sound(ACTIVATE_ASTEROID)
        self.pterodactilo = pygame.mixer.Sound(PTERODACTILO)

    def generate_obstacle(self, obstacle_type):
        if obstacle_type == 0:
            cactus_type = 'SMALL'
            obstacle = Cactus(cactus_type)
        elif obstacle_type == 1:
            cactus_type = 'LARGE'
            obstacle = Cactus(cactus_type)
        elif obstacle_type == 2:
            obstacle = Bird()
            self.pterodactilo.play()
        else:
            obstacle = Asteroid()
            self.activate_asteroid.play()
        return obstacle
    
    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.randint(0, 3)
            obstacle = self.generate_obstacle(obstacle_type)
            self.obstacles.append(obstacle)
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed)
        
            if obstacle.rect.x <- obstacle.rect.width:
                self.obstacles.pop()

            if game.player.type == SHIELD_TYPE:
                if game.player.rect.colliderect(obstacle.rect):
                    self.obstacles.pop()
                    self.destruction.play()
            elif game.player.rect.colliderect(obstacle.rect):
                if game.player.lifes > 1:
                    game.player.lifes -= 1
                    self.obstacles.pop()
                    self.dino_colliderect.play()
                else:
                    self.die.play()  
                    game.music.stop()            
                    game.playing = False
                    game.counter += 1
                    game.player.move_to_origin_pos()
                    game.player.hammer = []
                    game.power_up_manager.reset_powers_up()
                    game.background_color = (255, 255, 255)
            
            if len(game.player.hammer) > 0:
                game.power_up_manager.reset_powers_up
                if game.player.hammer[0].rect.colliderect(obstacle.rect):
                    self.obstacles.remove(obstacle)
                    self.destruction.play()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def remove_obstacles(self):
        self.obstacles = []