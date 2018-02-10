import pygame
import sys

class Controller:
	def __init__ (self, width=990, height=720):
        	#initialize pygame and pygame mixer for sounds
		pygame.init()
		pygame.mixer.init()
		#Set up screen size, caption, background
		self.width=width
		self.height=height
		self.screen=pygame.display.set_mode((self.width, self.height))
		self.caption=pygame.display.set_caption('Breaking The Glass Ceiling')
		self.background = pygame.Surface(self.screen.get_size()).convert()


	def startGame(self):
		end_it=True
		while (end_it==True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					end_it=False
			self.background.fill((0, 0, 0))
			self.screen.blit(self.background, (0,0))
			pygame.display.flip()
		pygame.quit()


def main():
	main_window=Controller()
	main_window.startGame()

main()


