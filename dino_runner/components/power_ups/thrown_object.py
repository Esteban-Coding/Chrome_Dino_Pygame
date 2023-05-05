from pygame.sprite import Sprite

class Thrown_Object(Sprite):
    def __init__(self, object_to_thrown, x_pos, y_pos):
        self.image = object_to_thrown
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
    
    def update(self):
        self.rect.x += 20

    def draw(self, screen):
        screen.blit(self.image, self.rect)