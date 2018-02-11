import pygame


class Woman(pygame.sprite.Sprite):
	def __init__(self, x, y, img_file):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img_file).convert()
		self.image = pygame.transform.scale(self.image, (30,23))
		self.rect = self.image.get_rect()
		self.rect.centerx=x
		self.rect.centery=y
	
	def canMove(self, walls):
		if pygame.sprite.spritecollide(self, walls, False):
			return False
		return True

