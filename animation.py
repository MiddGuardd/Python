import pygame

class AnimateSprite(pygame.sprite.Sprite):
	
	def __init__(self, sprite_name, size=(200, 200)):
		super().__init__()
		self.size = size
		self.image = pygame.image.load(f'assets/{sprite_name}.png')
		self.image = pygame.transform.scale(self.image, size)
		self.current_image = 0 #commencer à l'image zéro
		self.images = animations.get(sprite_name)
		self.animation = False

	#Définir une méthode pour démarrer l'animation
	def start_animation(self):
		self.animation = True
	
	#définir une méthode pour animer le sprite
	def animate(self, loop=False):
		#Vérifier si l'animation est active
		if self.animation:
			#passer à l'image suivante
			self.current_image += 1
			#Vérifier si on a atteint la fin de l'animation
			if self.current_image >= len(self.images):
				#remettre l'animation au départ
				self.current_image = 0
				#Vérifier si l'anim n'est pas en mode boucle
				if loop is False:
					#Désactivation de l'animation
					self.animation = False
			#modifier l'image de l'animation précédente par la suivante
			self.image = self.images[self.current_image]
			self.image = pygame.transform.scale(self.image, self.size)


#définir une fonction pour charger les images
def load_animaton_images(sprite_name):
	#charger les 24 images du srpite
	images = []
	#récupérer le chemin du dossier
	path = f"assets/{sprite_name}/{sprite_name}"
	#boucler sur chaque image dans ce dossier
	for num in range(1, 24):
		image_path = path + str(num) + '.png'
		images.append(pygame.image.load(image_path))
		#renvoyer le contenu de la liste
	return images

#Définir un dictionnaire qui va contenir les images chargées de chaque sprite
#mummy -> [...mummy1.png, ...mummy2.png, ....] meme systeme pour player
animations = {
	'mummy': load_animaton_images('mummy'),
	'player': load_animaton_images('player'),
	'alien': load_animaton_images('alien')
}