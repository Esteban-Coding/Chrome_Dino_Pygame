import sys
import pygame

from dino_runner.utils.constants import BG, DEFAULT_TYPE, PLAY, HAMMER_TYPE, ICON, INITIAL_GAME_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, POINTS, MUSIC, LOBBY
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacle_manager import ObstacleManager
from dino_runner.components.power_up_manager import PowerUpManager
from dino_runner.components.cloud import Cloud
from dino_runner.utils.text_utils import get_lifes, get_score_element, get_centered_message, get_max_score, get_counter, get_game_over, get_play_again, get_power_up_time, get_notify_use_power

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = INITIAL_GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.background_color = (255, 255, 255)
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.cloud = Cloud()
        self.points = 0
        self.counter = 0
        self.max_points = 0

        self.points_sound = pygame.mixer.Sound(POINTS)
        self.points_sound.set_volume(0.3)
        self.music = pygame.mixer.Sound(MUSIC)
        self.music.set_volume(0.1)
        self.lobby = pygame.mixer.Sound(LOBBY)
        self.lobby.set_volume(0.1)
        self.play_sound = pygame.mixer.Sound(PLAY)
    
    def show_score(self):
        self.points += 1
        if self.max_points <= self.points:
            self.max_points = self.points

        if self.points % 50 == 0:
            self.game_speed += 1

        if self.points % 100 == 0:
            self.points_sound.play()

        score, rect = get_score_element(self.points, self.playing)
        self.screen.blit(score, rect)
    
    def show_lifes(self):
        if self.player.lifes >= 1:
            lifes, rect = get_lifes(20, 20)
            self.screen.blit(lifes, rect)
        if self.player.lifes >= 2:
            lifes, rect = get_lifes(50, 20)
            self.screen.blit(lifes, rect)
        if self.player.lifes >= 3:
            lifes, rect = get_lifes(80, 20)
            self.screen.blit(lifes, rect)
        if self.player.lifes >= 4:
            lifes, rect = get_lifes(110, 20)
            self.screen.blit(lifes, rect)
        if self.player.lifes >= 5:
            lifes, rect = get_lifes(140, 20)
            self.screen.blit(lifes, rect)
    
    def show_menu(self):
        self.lobby.play(50)
        self.screen.fill((255, 255, 255))
        if self.counter == 0:
            text, rect = get_centered_message("Press any KEY to Start!")
            self.screen.blit(text, rect)
        else:
            text, rect = get_game_over()
            self.screen.blit(text, rect)
            text, rect = get_play_again()
            self.screen.blit(text, rect)
            text, rect = get_score_element(self.points, self.playing)
            self.screen.blit(text, rect)
            text, rect = get_max_score(self.max_points)
            self.screen.blit(text, rect)
            text, rect = get_counter(self.counter)
            self.screen.blit(text, rect)

        pygame.display.update()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.lobby.stop()
                self.play_sound.play()
                self.music.play(100)
                self.points = 0
                self.run()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.obstacle_manager.remove_obstacles()
        self.game_speed = INITIAL_GAME_SPEED

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update(self):
        self.user_input = pygame.key.get_pressed()
        self.player.update(self.user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.cloud.update(self.game_speed)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(self.background_color)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        self.show_score()
        self.show_lifes()
        self.draw_power_up_time()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        if self.points % 500 == 0 and self.points > 0:
            if self.background_color == (255, 255, 255):
                self.background_color = (105, 105, 105)
            else:
                self.background_color = (255, 255, 255)

    def draw_power_up_time(self):
        if self.player.type != DEFAULT_TYPE:
            time = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 1)
            if time >= 0.1:
                text, rect = get_power_up_time(self.player.type, time)
                self.screen.blit(text, rect)
                if self.player.type == HAMMER_TYPE:
                    text, rect = get_notify_use_power()
                    self.screen.blit(text, rect)
            else:
                self.player.power_up_time = 0
                self.player.type = DEFAULT_TYPE
