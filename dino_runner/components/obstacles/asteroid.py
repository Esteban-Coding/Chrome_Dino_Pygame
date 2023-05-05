import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import ASTEROID

class Asteroid(Obstacle):
    ASTEROID_SPEED = [10, 20, 30]

    def __init__(self):
        self.type = 0
        self.speed = self.ASTEROID_SPEED[random.randint(0, 2)]
        super().__init__(ASTEROID, self.type) 
        self.rect.y = 0

    def draw(self, screen):
        screen.blit(ASTEROID[0], self.rect)
        
        if self.rect.y < 350:
            self.rect.y += self.speed
            