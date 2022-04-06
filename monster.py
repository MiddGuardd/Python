import pygame
import random
import animation

class Monster(animation.AnimateSprite):

	def __init__(self, game, name, size, offset=0):
		super().__init__(name, size)
		self.game = game
		self.health = 100
		self.max_health = 100
		self.atk = 0.3
		self.rect = self.image.get_rect()
		self.rect.x = 1000 + random.randint(0, 300)
		self.rect.y = 540 - offset
		self.loot_amount = 10
		self.start_animation()

	def set_speed(self, speed):
		self.default_speed = speed
		self.velocity = random.randint(1, 3)

	def set_loot_amount(self, amount):
		self.loot_amount = amount

	def damage(self, amount):
		#Pour infliger des dégâts au monstre
		self.health -= amount

		#Vérifier si ses PV atteignent 0
		if self.health <= 0:
			#On le fait respawn
			self.rect.x = 1000 + random.randint(0, 300)
			self.health = self.max_health
			self.velocity = random.randint(1, self.default_speed)
			#ajouter des pts au score
			self.game.add_score(self.loot_amount)

		#Si la barre d'event est chargée au max
		if self.game.comet_event.is_full_loaded():
			self.game.all_monsters.remove(self)


			#Appel de la méthode pour tenter de déclencher la pluie
			self.game.comet_event.attempt_fall()

	def update_animation(self):
		self.animate(loop=True)

	def update_health_bar(self, surface):
	
		pygame.draw.rect(surface, (50, 50, 50), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
		pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


	def forward(self):
		#Si l emonstre n'entre pas en contact avec le joueur il s'avance
		if not self.game.check_collision(self, self.game.all_players): 
			self.rect.x -= self.velocity
		#Sinon il s'arrête et inflige des dégâts au joueur
		else:
			self.game.player.damage(self.atk)

#définir classe momie
class Mummy(Monster):

	def __init__(self, game):
		super().__init__(game, "mummy", (130, 130))
		self.set_speed(3)
		self.set_loot_amount(20)

#Définir classe alien
class Alien(Monster):

	def __init__(self, game):
		super().__init__(game, "alien", (300, 300), 120)
		self.health = 250
		self.max_health = 250
		self.atk = 0.8
		self.set_speed(1)
		self.set_loot_amount(80)