import board

class Player:
  def __init__(self, x, y, id):
    self.x = x
    self.y = y
    self.vx = 0
    self.vy = 0
    self.id = id

  def update(self,playerid):
    self.x += self.vx
    self.y += self.vy

    if self.x > board.WIDTH - 50:
      self.x = board.WIDTH - 50
    if self.x < 0:
      self.x = 0
    if self.y > board.HEIGHT - 50:
      self.y = board.HEIGHT - 50
    if self.y < 0:
      self.y = 0

    if self.id == 0:
      self.id = playerid

  def render(self,screen,sprites):
    screen.blit(sprites[self.id % 4], (self.x, self.y))