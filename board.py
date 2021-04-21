import pygame

#hexagonal board

WIDTH  = 800
HEIGHT = 600

EmeraldPeak_S = pygame.image.load('images/tiles/EmeraldPeak.png')
JungleDock_S = pygame.image.load('images/tiles/JungleDock.png')

class Grid:
	def __init__(self):
		self.grid = [[None,None,None],
					 [None,None,None,None],
					 [None,None,None,None,None],
					 [None,None,None,None],
					 [None,None,None]]
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

	def render(self):
		pass

