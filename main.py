import pygame
import sys
import office
import wall
import woman
import men

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

		self.create_office=office.Office(30,23)
		self.office_background=office.Office.createOffice(self.create_office)
		self.wall_sprites = pygame.sprite.Group(self.office_background[0])
		self.floor_sprites= pygame.sprite.Group(self.office_background[1])

		self.woman=woman.Woman(90,46, "BlondeHair.png")
		self.woman_sprite=pygame.sprite.Group(self.woman)

		self.man1=men.men(880,450,'man1.png') #done CEO/BOSS
		self.man2=men.men(150,50,'man2.png') #done
		self.man3=men.men(280,40,'man3.png') #done
		self.man4=men.men(460,40,'man4.png') #done
		self.man5=men.men(640,40,'man5.png') #done
		self.man6=men.men(765,40,'man6.png') #done
		self.man7=men.men(880,40,'man7.png') #done
		self.man8=men.men(480,207,'man8.png') #done
		self.man9=men.men(480,253,'man9.png') #done
		self.man10=men.men(720,207,'man10.png') #done
		self.man11=men.men(600,253,'man11.png') #done
		self.man12=men.men(720,253,'man12.png') #done
		self.man13=men.men(60,130,'man13.png') #done
		self.man14=men.men(60,450,'man14.png') #done
		self.man15=men.men(60,300,'man15.png') #done

	#	self.menList = []
	#	for i in range(1,16):
	#		self.menList.append(self.man + i)
		self.men_sprite=pygame.sprite.Group([self.man1,self.man2,self.man3,self.man4,self.man5,self.man6,self.man7,self.man8,self.man9,self.man10,self.man11,self.man12,self.man13,self.man14,self.man15])


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
				if action=="OFFICE":
					self.goToOffice()
				if action=="QUIT":
					pygame.quit()
		else:
			pygame.draw.rect(self.screen, ic,(x,y,w,h))
		pygame.font.init()
		smallText = pygame.font.SysFont("Calibri", 28, True, False)
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
			newgame = self.button("Start Game", 420,350,150,130,BLACK,WHITE, "OFFICE")
			self.background = pygame.image.load("Title screen.png")
			self.screen.blit(pygame.transform.scale(self.background, (990, 624)), (0,0))

			myfont=pygame.font.SysFont("Calibri", 50, True, False)
			nlabel=myfont.render("Start", False, BLACK)
			self.screen.blit(nlabel, (440,385))


			pygame.display.flip()
		pygame.quit()

	def goToOffice(self):
		end_it=True
		while (end_it==True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					end_it=False
				if event.type == pygame.KEYDOWN:
					if event.key==pygame.K_UP and self.woman.canMove(self.wall_sprites):
						self.woman.rect.y-=23
						self.woman.direction="up"
					elif event.key==pygame.K_DOWN and self.woman.canMove(self.wall_sprites):
						self.woman.rect.y+=23
						self.woman.direction="down"
					elif event.key==pygame.K_LEFT and self.woman.canMove(self.wall_sprites):
						self.woman.rect.x-=30
						self.woman.direction="left"
					elif event.key==pygame.K_RIGHT and self.woman.canMove(self.wall_sprites):
						self.woman.rect.x+=30
						self.woman.direction="right"
				if self.woman.canMove(self.wall_sprites)==False:
					if self.woman.direction=="up":
						self.woman.rect.y+=23
					if self.woman.direction=="down":
						self.woman.rect.y-=23
					if self.woman.direction=="left":
						self.woman.rect.x+=30
					if self.woman.direction=="right":
						self.woman.rect.x-=30




			self.background = pygame.Surface(self.screen.get_size()).convert()
			self.background.fill((250, 250, 250))
			self.screen.blit(self.background,(0,0))
			self.wall_sprites.draw(self.screen)
			self.floor_sprites.draw(self.screen)
			self.woman_sprite.draw(self.screen)

			self.men_sprite.draw(self.screen)

			pygame.display.flip()
		pygame.quit()






def main():
	main_window=Controller()
	main_window.startGame()

main()
