import pygame

class men(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        '''
        Initializes men
        '''
        #intialize the sprite
        pygame.sprite.Sprite.__init__(self)
        #loads the image and creates a surface
        self.image = pygame.image.load(img_file).convert_alpha()
        #scales the image to be the same as the tile size which is 15x15
        self.image = pygame.transform.scale(self.image, (30,23)).convert_alpha()
        #rectangle surface
        self.rect = self.image.get_rect()
        #x value of rectangle
        self.rect.x = x
        #y value of rectangle
        self.rect.y = y
