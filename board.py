import pygame
import random

#hexagonal board

WIDTH  = 800
HEIGHT = 600

class Grid:
	def __init__(self,list = [None]*19):
		self.grid = [list[0:3],
					list[3:7],
					list[7:12],
					list[12:16],
					list[16:19]]
	def get(self,E,S):
		if S<0 or S>len(self.grid):
			return "S Out of Bounds"
		#accommodate bend
		x = int(E-abs(S-2)/2)
		if x<0 or x>len(self.grid[S]):
			return "E Out of Bounds"
		return self.grid[S][x]

	def set(self,E,S,V):
		if S<0 or S>len(self.grid):
			return "S Out of Bounds"
		#accommodate bend
		x = int(E-abs(S-2)/2)
		if x<0 or x>len(self.grid[S]):
			return "E Out of Bounds"
		self.grid[S][x] = V
		return self.grid[S][x]

	def position(self,S,x):
		return [S,x+abs(S-2)/2]

	def str(self):
		output = ""
		for row in self.grid:
			output+=row+"\n"

	@staticmethod
	def x2e(S,x):
		return x+abs(S-2)/2

	@staticmethod
	def e2x(S,E):
		return int(E-abs(S-2)/2)

	@staticmethod
	def l2e(L):
		return Grid.x2e(L[1],L[0])
	@staticmethod
	def l2y(L):
		return L[1]
	@staticmethod
	def l2x(L):
		return int(Grid.l2e(L)-abs(Grid.l2y(L)-2)/2)


class Tile:
	def __init__(self,name,description,spritePath,location=None):
		self.name = name
		self.description = description
		self.sprite = pygame.image.load(spritePath)

		if location:
			self.place(location)

	def place(self,L):
		self.L = L
		self.E = Grid.l2e(L)
		self.S = Grid.l2y(L)
		self.X = Grid.l2x(L)

class Board:

	def __init__(self):
		Tiles = [
		Tile("Stepped Pyramid",
			"""I came upon a tomb built of large hewn stones and covered in vines.""",
			"images/tiles/VerdantGlade.png"),
		
		Tile("Weathered Pyramid",
			"""An old pyramid of brown stone stands in the jungle.""",
			"images/tiles/VerdantGlade.png"),
		
		Tile("Lush Glade",
			"""Bright vegetation surrounds a peaceful glade.""",
			"images/tiles/LushGlade.png"),

		Tile("Verdant Glade",
			"""Light filters through the canopy to illuminate a quiet clearing.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Emerald Peak",
			"""A treacherous, heavily forested, peak towers above you.""",
			"images/tiles/EmeraldPeak.png"),
		
		Tile("Jade Peak",
			"""A stark stone peak rises out of the jungle canopy.""",
			"images/tiles/EmeraldPeak.png"),

		Tile("Deep Cavern",
			"""There's an opening to a large cavern.
	It appears to have contained a large mining operation once.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Dark Cavern",
			"""A stream flows along the path and both dissappear into a sinkhole.
	The remains of a cooking fire are surrounded by bones.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Brilliant Understory",
			"""I'm surrounded by exotic and unfamiliar plants.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Tangled Understory",
			"""The trees are shrouded in curtains of vines.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Ominous Clearing",
			"""A carcass rests at the center of this clearing.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Gloomy Clearing",
			"""The floor of the jungle is clear here,
	but the canopy is unbroken and it's very dark""",
			"images/tiles/VerdantGlade.png"),

		Tile("Lost Hut",
			"""The ruins of a small hut are barely visible in the jungle.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Abandoned Village",
			"""Here's a villiage that appears to have been abandoned recently.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Wild Path",
			"""It looks like large animals have cut a path through the jungle.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Terrible Path",
			"""A path winds along a sheer cliff face.
	Every so often a rivulet descends forming muddy pools in the path.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Temple of the Jaguar",
			"""There's a temple with carvings of jaguars.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Temple of the Mask",
			"""There's a temple hung with frightful wooden masks.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Stony Bog",
			"""Flat stones rise from the bog here forming paths.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Fallen Bog",
			"""Trees are sinking into the mud, but I can move across their tops.""",
			"images/tiles/VerdantGlade.png"),

		Tile("Jungle Dock",
			"""I arrived at a dock in the heart of the jungle.
	While here I can manage the vegetation. If gone too long
	I can tell it will become overgrown.""",
			"images/tiles/JungleDock.png")]
		shuffledPlaces = Tiles[0:-1]
		random.shuffle(shuffledPlaces)
		self.tiles = Grid(shuffledPlaces[0:9]+[Tiles[-1]]+shuffledPlaces[10:19])
		for rowN in range(len(self.tiles.grid)):
			for colN in range(len(self.tiles.grid[rowN])):
				self.tiles.grid[rowN][colN].place([colN,rowN])

	def render(self,screen):
		for row in self.tiles.grid:
			for tile in row:
				screen.blit(tile.sprite, (tile.E*100+40,tile.S*50))

