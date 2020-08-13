from datetime import datetime
from Plateau import *
class Jeu:
	def __init__(self, joueur, plateau):
		"""
			Prend en paramètre un plateau de jeu
		"""
		self.joueur = joueur
		self.plateau = plateau

		while not plateau.est_tombe_balle:
			pass


	def commencer(self):
		"""
			¨Permet de lancer une partie
		"""
		self.plateau
		pygame.init()
	def stats(self):
		"""
			return une chaine de caracteres sous le format suivant:
			nom_joueur : score : date
		"""
		return "{} : {} : {}".format(self.joueur, self.plateau.score, datetime.now())


	def sauvegarder_jeu(self):
		"""
			Sauvegarde les stats d'un joueur
		"""
		with open("SCORES.txt", "at", encoding="utf8") as file:
			file.write(self.stats())

