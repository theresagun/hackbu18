import wall
import pygame

class Office:
	def __init__(self, x_tile_size, y_tile_size):
		self.office_file = open('office_map.txt', 'r')
		self.x_tile_size=x_tile_size
		self.y_tile_size=y_tile_size

	def createOffice(self):
		self.tiles=[]
		for line in self.office_file:
			self.tiles.append(list(line.rstrip()))
		self.office_file.close()

		self.wall_list=[]
		self.floor_list=[]
		for row in range(len(self.tiles)):
			for col in range(len(self.tiles[row])):
				if self.tiles[row][col]=="1":
					self.wall_list.append(wall.Wall(row*self.x_tile_size,col*self.y_tile_size, 'black-rect.jpg'))
				elif self.tiles[row][col]=="0":
					self.floor_list.append(wall.Wall(row*self.x_tile_size,col*self.y_tile_size, 'wood-background.png'))
		return self.wall_list, self.floor_list



#####FOR MAIN
#	self.create_office=office.Office(30,24)
#	self.map_background=office.Office.createOffice(self.create_office)
#	self.wall_sprites = pygame.sprite.Group(self.map_background)

#	self.wall_sprites.draw(self.screen)
