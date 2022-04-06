import pygame
from projectile import Projectile
import animation

#Créer la classe "joueur"
class Player(animation.AnimateSprite):
	def __init__(self, game):
		super().__init__('player')
		self.game = game
		self.health = 100 #On définit ici la variable représantant le nombre de points vie du joueur
		self.max_health = 100 #Ici le nombre de points de vie maximum du joueur
		self.atk = 10 #Ici la valeur d'attaque du joueur
		self.velocity = 4 #Ici la vitesse de déplacement en pixels
		self.all_projectiles = pygame.sprite.Group()
		self.rect = self.image.get_rect() #Permet de controler le déplacement du joueur
		self.rect.x = 400
		self.rect.y = 500

	def damage(self, amount):
		if self.health - amount > amount:
			self.health -= amount
		else:
			#Si le joueur n'a plus de pv
			self.game.game_over()

	def update_animation(self):
		self.animate()

	def update_health_bar(self, surface):
	
		pygame.draw.rect(surface, (50, 50, 50), [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])
		pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 5])


	def launch_projectile(self):
		self.all_projectiles.add(Projectile(self))
		#Démarer l'animation du lancer
		self.start_animation()
		self.game.sound_manager.play('tir')

	def move_right(self):
		if not self.game.check_collision(self, self.game.all_monsters):
			self.rect.x += self.velocity

	def move_left(self):
		self.rect.x -= self.velocity