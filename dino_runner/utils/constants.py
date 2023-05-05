import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

ASTEROID = [pygame.image.load(os.path.join(IMG_DIR, 'Other/Asteroid.png'))]

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
HEART_TYPE = "heart"

INITIAL_GAME_SPEED = 20

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))
RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))

POINTS = (os.path.join(IMG_DIR, 'SFX/point.wav'))
JUMP_SOUND = (os.path.join(IMG_DIR, 'SFX/jump.wav'))
GAME_OVER_SOUND = (os.path.join(IMG_DIR, 'SFX/die.wav'))
MUSIC = (os.path.join(IMG_DIR, 'SFX/music.mp3'))
LOBBY = (os.path.join(IMG_DIR, 'SFX/lobby.mp3'))
ACTIVATE_SHIELD = (os.path.join(IMG_DIR, 'SFX/activate_shield.wav'))
ACTIVATE_HAMMER = (os.path.join(IMG_DIR, 'SFX/activate_hammer.wav'))
THROWN_HAMMER = (os.path.join(IMG_DIR, 'SFX/thrown_hammer.wav'))
ACTIVATE_HEART = (os.path.join(IMG_DIR, 'SFX/activate_heart.wav'))
DINO_COLLIDERECT = (os.path.join(IMG_DIR, 'SFX/dino_colliderect.wav'))
DESTRUCTION = (os.path.join(IMG_DIR, 'SFX/destruction.wav'))
ACTIVATE_ASTEROID = (os.path.join(IMG_DIR, 'SFX/activate_asteroid.wav'))
PTERODACTILO = (os.path.join(IMG_DIR, 'SFX/pterodactilo.wav'))
PLAY = (os.path.join(IMG_DIR, 'SFX/play.wav'))
