import pygame
from player import Player
from monster import Mummy
from monster import Alien
from comet_event import CometFallEvent
from sounds import SoundManager

#Créer la classe "game" qui représente le jeu
class Game:
	def __init__(self, screen):
		#Définir si le jeu a commencé ou non
		self.is_playing = False
		#Générer le joueur
		self.all_players = pygame.sprite.Group()
		self.player = Player(self)
		self.all_players.add(self.player)
		#Générer l'event
		self.comet_event = CometFallEvent(self)
		#Générer les monstres
		self.all_monsters = pygame.sprite.Group()
		#Gérer le son
		self.sound_manager = SoundManager()
		#mettre le score à zéro
		self.font = pygame.font.SysFont("monospace", 16)
		self.score= 0
		self.pressed = {}
	

	def start(self):
		self.is_playing = True
		self.spawn_monster(Mummy)
		self.spawn_monster(Mummy)
		self.spawn_monster(Alien)

	def add_score(self, points):
		self.score += points


	def game_over(self):
		#Remettre le jeu à zéro
		self.all_monsters = pygame.sprite.Group()
		self.comet_event.all_comets = pygame.sprite.Group()
		self.player.health = self.player.max_health
		self.comet_event.reset_percent()
		self.is_playing = False
		self.score = 0
		self.sound_manager.play('game_over')


	def update(self, screen):
		#afficher le score
		score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
		screen.blit(score_text, (20, 20))

		#On affiche le joueur
		screen.blit(self.player.image, self.player.rect)

		#Actualiser la barre de vie du joueur
		self.player.update_health_bar(screen)

		#Actualiser la barre d'event
		self.comet_event.update_bar(screen)

		#Actualiser l'animation du joueur
		self.player.update_animation()

		#On récupère les projectiles
		for projectile in self.player.all_projectiles:
			projectile.move()


		#On récupère les monstres
		for monster in self.all_monsters:
			monster.forward()
			monster.update_health_bar(screen)
			monster.update_animation()

		#On récupère les comètes
		for comet in self.comet_event.all_comets:
			comet.fall()

		#On affiche le(s) projectile(s)
		self.player.all_projectiles.draw(screen)

		#On affiche le(s) monstre(s)
		self.all_monsters.draw(screen)

		#Appliquer l'ensemble des images de mon groupe de comètes
		self.comet_event.all_comets.draw(screen)
	
		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x+self.player.rect.width < screen.get_width():
			self.player.move_right()
		elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
			self.player.move_left()

	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

	def spawn_monster(self, monster_class_name):
		self.all_monsters.add(monster_class_name.__call__(self))