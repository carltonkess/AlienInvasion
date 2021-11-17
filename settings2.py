class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's static settings."""

		# S c r e e n  S e t t i n g s 
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (00,00,255)

		# S h i p  S e t t i n g s 
		self.ship_speed = 10.5
		self.ship_limit = 3

		# B u l l e t  S e t t i n g s 
		self.bullet_speed = 15.0
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = (230, 60, 60)
		self.bullets_allowed = 6

		# A l i e n  S e t t i n g s 
		self.fleet_drop_speed = 10

		# How quickly the game speeds up
		self.speedup_scale = 1.1

		# How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed = 10.5
		self.bullet_speed = 15.0
		self.alien_speed = 1.0

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# S c o r i n g 
		self.alien_points = 50
		

	def increase_speed(self):
		"""Increae speed settings and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.bullet_width *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)