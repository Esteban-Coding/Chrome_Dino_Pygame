import pygame

from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_OVER, RESET, HEART

FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0, 0, 0)

def get_score_element(score, playing):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(f"Points: {score}", True, BLACK_COLOR)
    rect = text.get_rect()
    if playing:
        rect.center = (1000, 30)
    else:
        rect.center = (SCREEN_WIDTH // 2, 450)
    return text, rect

def get_centered_message(message):
    font = pygame.font.Font(FONT_STYLE, 40)
    text = font.render(message, True, BLACK_COLOR)
    rect = text.get_rect()
    rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    return text, rect

def get_game_over():
    text = GAME_OVER
    rect = text.get_rect()
    rect.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) - 50)
    return text, rect

def get_play_again():
    text = RESET
    rect = text.get_rect()
    rect.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 50)
    return text, rect

def get_max_score(high_score):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(f"Highest score: {high_score}", True, BLACK_COLOR)
    rect = text.get_rect()
    rect.center = (SCREEN_WIDTH // 2, 500)
    return text, rect

def get_counter(counter):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(f"Deaths: {counter}", True, BLACK_COLOR)
    rect = text.get_rect()
    rect.center = (SCREEN_WIDTH // 2, 550)
    return text, rect

def get_power_up_time(type_power_up, time_power_up):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(f'{type_power_up.capitalize()} enabled for {time_power_up} seconds', True, BLACK_COLOR)
    rect = text.get_rect()
    rect.center = (SCREEN_WIDTH // 2, 30)
    return text, rect

def get_notify_use_power():
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render('Press E to use Power', True, BLACK_COLOR)
    rect = text.get_rect()
    rect.center = (SCREEN_WIDTH // 2, 550)
    return text, rect

def get_lifes(x, y):
    text = HEART
    rect = text.get_rect()
    rect.center = (x, y)
    return text, rect