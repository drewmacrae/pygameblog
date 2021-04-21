import pygame, sys
from pygame.locals import *
import pickle
import select
import socket
import player
import board

BUFFERSIZE = 2048

screen = pygame.display.set_mode((board.WIDTH, board.HEIGHT))
pygame.display.set_caption('Forgotten Jungle')

clock = pygame.time.Clock()

serverAddr = '127.0.0.1'
if len(sys.argv) == 2:
  serverAddr = sys.argv[1]

sprite1 = pygame.image.load('images/Pip32.png')
sprite2 = pygame.image.load('images/tiles/EmeraldPeak100.png')
sprite3 = pygame.image.load('images/tiles/JungleDock.png')
sprite4 = pygame.image.load('images/Pip32.png')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverAddr, 4321))

playerid = 0

sprites = { 0: sprite1, 1: sprite2, 2: sprite3, 3: sprite4 }


#game events
#['event type', param1, param2]
#
#event types: 
# id update 
# ['id update', id]
#
# player locations
# ['player locations', [id, x, y], [id, x, y] ...]

#user commands
# position update
# ['position update', id, x, y]

class GameEvent:
  def __init__(self, vx, vy):
    self.vx = vx
    self.vy = vy

cc = player.Player(50, 50, 0)

minions = []

while True:
  ins, outs, ex = select.select([s], [], [], 0)
  for inm in ins: 
    gameEvent = pickle.loads(inm.recv(BUFFERSIZE))
    if gameEvent[0] == 'id update':
      playerid = gameEvent[1]
      print(playerid)
    if gameEvent[0] == 'player locations':
      gameEvent.pop(0)
      minions = []
      for minion in gameEvent:
        if minion[0] != playerid:
          minions.append(player.Player(minion[1], minion[2], minion[0]))
    
  for event in pygame.event.get():
    if event.type == QUIT:
    	pygame.quit()
    	sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_LEFT: cc.vx = -10
      if event.key == K_RIGHT: cc.vx = 10
      if event.key == K_UP: cc.vy = -10
      if event.key == K_DOWN: cc.vy = 10
    if event.type == KEYUP:
      if event.key == K_LEFT and cc.vx == -10: cc.vx = 0
      if event.key == K_RIGHT and cc.vx == 10: cc.vx = 0
      if event.key == K_UP and cc.vy == -10: cc.vy = 0
      if event.key == K_DOWN and cc.vy == 10: cc.vy = 0

  clock.tick(60)
  screen.fill((255,255,255))

  cc.update(playerid)

  for m in minions:
    m.render(screen,sprites)

  cc.render(screen,sprites)

  pygame.display.flip()

  ge = ['position update', playerid, cc.x, cc.y]
  s.send(pickle.dumps(ge))
s.close()
