import breakout
import snake
#import sys
#sys.path.append('FloodIt-master')
#import game

def breakout1(level):
	if(not breakout.main(level)):
		return 0
	else:
		return 10

def snake1(level):
	return snake.main(level)

#def floodIt():
	#return game.main()
