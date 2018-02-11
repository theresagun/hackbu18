import breakout
import snake
import sys
import pygame

#sys.path.append('interactions/Level1_interactions')
#import



def converse(level, previous_num, screen, controller):
	end_it=True
	while end_it==True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end_it=False
		bob1=open('interactions/Level1_interactions/Bob1.txt', 'r')
		bob2=open('interactions/Level1_interactions/Bob2.txt', 'r')
		#.....
		font=pygame.font.SysFont("Times New Roman", 40)
	 
		print_out=""
		for line in bob1:
			print_out+=line+ '\n'
		print(print_out)
		nlabel=font.render(print_out, False, (0,0,0)) 
			
		#breakout1(level)
		controller.screen.blit(nlabel, (20,560))
		
	

def breakout1(level):
	
	if(not breakout.main(level)):
		return 0
	else:
		return 10

def snake1(level):
	return snake.main(level)

#def floodIt():
	#return game.main()
