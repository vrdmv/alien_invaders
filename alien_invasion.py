import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship 
import game_functions as gf

def run_game():
	"""Initialize the game and create a screen object."""
	pygame.init()
	alinv_settings = Settings()
	screen = pygame.display.set_mode(
		(alinv_settings.screen_width, alinv_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#Make a ship.
	ship = Ship(alinv_settings, screen)
	#Make a group to store bullets in.
	bullets = Group()
	#Make an alien
	aliens = Group()
	#Make the Play button.
	play_button = Button(alinv_settings, screen, "Play")
	
	#Create the fleet of aliens.
	gf.create_fleet(alinv_settings, screen, ship, aliens)
	
	#Set the background color.
	background_color = (230, 230, 230)
	
	#Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(alinv_settings)
	sb = Scoreboard(alinv_settings, screen, stats)

	#Start the main loop for the game.
	active = True 
	while active: 
		gf.check_events(alinv_settings, screen, stats, sb, play_button, ship,
			aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(alinv_settings, screen, stats, sb, ship, aliens,
				bullets)
			gf.update_aliens(alinv_settings, screen, stats, sb, ship, aliens,
				bullets)
			
		gf.update_screen(alinv_settings, screen, stats, sb, ship, aliens,
			bullets, play_button)

run_game()

