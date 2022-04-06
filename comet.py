import pygame
import random

class Comet(pygame.sprite.Sprite):

	def __init__(self, comet_event):
		super().__init__()
		#Définir le sprite
		self.image = pygame.image.load('assets/comet.png')
		self.rect = self.image.get_rect()
		self.velocity = random.randint(1, 3)
		self.rect.x = random.randint(20, 800)
		self.rect.y = - random.randint(0, 800)
		self.comet_event = comet_event

	def remove(self):
		self.comet_event.all_comets.remove(self)
		self.comet_event.game.sound_manager.play('meteorite')

		#Vérifier si le nombre de comète vaut zéro
		if len(self.comet_event.all_comets) == 0:
			print("Fini")
			#Remettre la barre à zéro
			self.comet_event.reset_percent()
			#On fait respawn les monstres
			self.comet_event.game.start()

	def fall(self):
		self.rect.y += self.velocity

		 #Ne tombe pas sur le sol
		if self.rect.y >= 500:
		 	print("sol")
		 	#Retirer la boule de feu
		 	self.remove()
		#Si il n'y a plsu de boules de feu sur le jeu
		if len(self.comet_event.all_comets) == 0:
			print("L'event est fini")
			self.comet_event.reset_percent()
			self.comet_event.fall_mode = False

		#Verifier si  la boule touche le joueur
		if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
			print("joueur touché")
			self.remove()
			#Subir des dégats au joueur
			self.comet_event.game.player.damage(20)