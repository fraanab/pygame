import sys

import pygame
from level import Level
from pygame.locals import *
from settings import *


class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
		pygame.display.set_caption('Hard Drugs')
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):
		while True:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			dt = self.clock.tick() / 1000

			self.level.run(dt)

			# Update frame
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()
