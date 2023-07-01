import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The Cocainer")
clock = pygame.time.Clock()
running = True

player_movement_sheet = pygame.image.load("C:/Users/fraan/Desktop/pygame/Sprout Lands - Sprites - Basic pack/Characters/Basic Charakter Spritesheet.png").convert()
sprite_w = 16
sprite_h = 16
sprite_frames = []
for y in range(0, player_movement_sheet.get_height(), sprite_h):
	for x in range(0, player_movement_sheet.get_width(), sprite_w):
		sprite_frames.append(player_movement_sheet.subsurface(pygame.Rect(x, y, sprite_w, sprite_h)))

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()

		self.frames = sprite_frames
		self.current_frame = 0

		self.image = self.frames[self.current_frame]

		# self.image = pygame.Surface((32, 32))
		# self.image.fill((255,0,0))

		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

		self.speed = 5
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.rect.x -= self.speed
		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed
		if keys[pygame.K_UP]:
			self.rect.y -= self.speed
		if keys[pygame.K_DOWN]:
			self.rect.y += self.speed

		self.current_frame = (self.current_frame + 1) % len(self.frames)
		self.image = self.frames[self.current_frame]

player = Player(200, 200)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while running:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:					# if user clicked X
			running = False

	all_sprites.update()
	screen.fill('white')								# fill screen with color to wipe last frame
	
	# RENDER GAME HERE

	all_sprites.draw(screen)
	pygame.display.flip()							# update frame ( screen )
	# pygame.display.update()						# update one element in the frame ( in the screen )

	clock.tick(60)									# 60 fps

pygame.quit()
