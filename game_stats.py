class GameStats():
	"""Track statistics for Alien Invasion."""
	
	def __init__(self, alinv_settings):
		"""Initialize statistics."""
		self.alinv_settings = alinv_settings
		self.reset_stats()
		self.high_score = 0

		#Start game in an inactive state.
		self.game_active = False
		
	def reset_stats(self):
		"""Initialize sttistics that can shange during the game."""
		self.ships_left = self.alinv_settings.ship_limit
		self.score = 0
		self.level = 1
