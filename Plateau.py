import pygame, sys


class Plateau:
	""" Modelisation de la fenetre du jeu """
	def __init__(self, dimension:tuple, background_color:str, palette, balle=None, title="Brick game"):
		
		### caracteristiques de la fenetre
		self.taille_fenetre_x, self.taille_fenetre_y = dimension
			# Graphique
		self.screen = pygame.display.set_mode(dimension)
		pygame.display.set_caption(title)
 		
		### Gestion du Jeu
		self.game_over = False

		## composant palette




		### reaction infinie au maintient d'une touche
		pygame.key.set_repeat(1,20)
		while True:
			pygame.display.flip()
			self.screen.fill(background_color)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:

					# J'avoue avoir fait un peu de bricolage sur ces conditions, pour le moment elles marchent bien
					ne_sortira_pas_à_droite = palette1.position_palette_x + palette1.longueur + palette1.vitesse <= self.taille_fenetre_x
					ne_sortira_pas_à_gauche = 0 <= palette1.position_palette_x - palette1.longueur//2 + palette1.vitesse
					
					if event.key == pygame.K_RIGHT:
						if ne_sortira_pas_à_droite:
							palette1.move_right()
					elif event.key == pygame.K_LEFT:
						if ne_sortira_pas_à_gauche:
							palette1.move_left()

			

			pygame.draw.rect(self.screen, palette1.color_palette, 
				(palette1.position_palette_x, palette1.position_palette_y, palette1.longueur, 5))
			print(palette1.position_palette_x, palette1.position_palette_y)
			


if __name__ == "__main__":
	from Palette import *
	# color 
	color_white = (255, 255, 255)
	color_blue = (0, 0, 255)

	# creation d'un objet palette
	palette1 = Palette(50, color_blue, (250, 485), 10)
	# creation d'un objet balle
	balle1 = Balle()

	
	Plateau((500, 500), color_white, palette1)
	pygame.init()