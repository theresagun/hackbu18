import pygame


class Woman:
	def __init__(self, x, y, img_file):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img_file).convert()
		self.image = pygame.transform.scale(self.image, (30,23))
		self.rect.x=x
		self.rect.y=y
	
	def canMove(self, walls):
		if pygame.sprite.spritecollide(self, walls, False):
			return False
		return True
