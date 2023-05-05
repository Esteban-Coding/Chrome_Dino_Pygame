import random
import pygame

from dino_runner.utils.constants import ACTIVATE_HEART, DEFAULT_TYPE, HAMMER, SHIELD, HEART, ACTIVATE_SHIELD, ACTIVATE_HAMMER
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart

class PowerUpManager:
    POWER_UP_PROBABILITY = 50
    
    def __init__(self):
        self.power_ups = []
        self.activate_shield = pygame.mixer.Sound(ACTIVATE_SHIELD)
        self.activate_hammer = pygame.mixer.Sound(ACTIVATE_HAMMER)
        self.activate_heart = pygame.mixer.Sound(ACTIVATE_HEART)

    def generate_power_up(self):
        if random.randint(0, 1000) < self.POWER_UP_PROBABILITY:
            POWERS = [Shield(SHIELD), Hammer(HAMMER), Heart(HEART)]
            self.power_ups.append(random.choice(POWERS))
    
    def update(self, game):
        if len(self.power_ups) == 0 and game.player.type == DEFAULT_TYPE:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed)

            if game.player.rect.colliderect(power_up.rect):
                if power_up.type == "heart":
                    if game.player.lifes < 5:
                        game.player.lifes += 1
                        self.activate_heart.play()
                else:
                    if power_up.type == "shield":
                        self.activate_shield.play()
                    if power_up.type == "hammer":
                        self.activate_hammer.play()
                    game.player.activate_power_up(power_up.type)
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_time = power_up.start_time + (random.randint(3, 7) * 1000)
                self.power_ups.pop()
            
            if power_up.rect.x <- power_up.rect.width:
                self.power_ups.pop()
        
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset_powers_up(self):
        self.power_ups = []