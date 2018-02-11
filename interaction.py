import breakout

def first(level):
	if(not breakout.main(level)):
		return 0
	else:
		return 10
