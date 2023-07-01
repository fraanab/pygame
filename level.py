import pygame
from player import Player
from settings import *


class Level:
	def __init__(self):

		# get surface from main.py display set_mode(w, h)
		self.display_surface = pygame.display.get_surface()

		# sprite groups to update sprites
		self.all_sprites = pygame.sprite.Group()

		self.setup()

	def setup(self):
		self.player = Player((400,300), self.all_sprites)

	def run(self, dt):
		self.display_surface.fill('white')
		self.all_sprites.draw(self.display_surface)
		self.all_sprites.update(dt)
