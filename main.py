import pygame
import sys

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

class Controller:
	def __init__ (self, width=990, height=624):
        	#initialize pygame and pygame mixer for sounds
		pygame.init()
		pygame.mixer.init()
		#Set up screen size, caption, background
		self.width=width
		self.height=height
		self.screen=pygame.display.set_mode((self.width, self.height))
		self.caption=pygame.display.set_caption('Breaking The Glass Ceiling')
		self.background = pygame.Surface(self.screen.get_size()).convert()


	def button(self, msg,x,y,w,h,ic,ac,action=None):
		'''
		Creates a button with font centered in it and functionality
		args:       msg     -   (str) text to be put on the button
					x       -   (int)x coordinate
                	y       -   (int)y coordinate
                	w       -   (int)width of the button
                	h       -   (int)height of the button
                	ic      -   (tuple)the numbers to decide on the lighter color when mouse isn't hovering over button
                	ac      -   (tuple)the numbers for the color when mouse is hovering over button
                	action  -   (str)word for what the button should do when clicked
    	return:     returns True or False to decide whether or not to close the window
    	'''
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		# print(click)

		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(self.screen, ac,(x,y,w,h))
			if(click[0] == 1 and action != None):
				if action=="play":
					gameStuff6.main()
				if action=="QUIT":
					pygame.quit()
		else:
			pygame.draw.rect(self.screen, ic,(x,y,w,h))

		smallText = pygame.font.SysFont("Helvetica", 28, True, False)
		newgame = smallText.render(msg, True, WHITE)
		space = smallText.size(msg)
		self.screen.blit(newgame, (x+(w-space[0])/2,y+(h-space[1])/2,w,h))

	def startGame(self):
		end_it=True
		while (end_it==True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					end_it=False
			self.background.fill((0, 0, 0))
			#self.screen.blit(self.background, (0,0))
			newgame = self.button("Start Game", 420,350,150,130,BLACK,WHITE, "QUIT")
			self.background = pygame.image.load("Title screen.png")
			self.screen.blit(pygame.transform.scale(self.background, (990, 624)), (0,0))

			myfont=pygame.font.SysFont("Calibri", 50, True, False)
			nlabel=myfont.render("Start", False, BLACK)
			self.screen.blit(nlabel, (440,385))

			pygame.display.flip()
		pygame.quit()




def main():
	main_window=Controller()
	main_window.startGame()

main()
