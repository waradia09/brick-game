class Palette:
    """ Modélisation de la palette """

    def __init__(self, longueur:int, couleur:str, position:tuple, vitesse:int):
        self._longueur_normale = longueur
        self.longueur = longueur
        self.position_x, self.position_y = position
        self.vitesse = vitesse
        self.color = couleur

    def move_right(self):
        """
            Allow the palette to move toward right
            :return:
        """
        self.position_x += self.vitesse

    def move_left(self):
        """
            Allow the palette to move toward left
            :return: (None)
        """
        self.position_x -= self.vitesse

    def evoluer(self, taille_plus:int):
        """
            Permet d'aggrandir la taille de la palette
            :return: (None)
        """
        self.longueur += taille_plus

    def evoluer_inverser(self, taille_moins):
        """
            Permet de diminuer la taille de la palette
            :return: (None)
        """
        self.longueur -= taille_moins

    def renitialise_normale(self):
        """
            Renitialise la taille de la palette
            :return: (None)
        """
        self.longueur = self._longueur_normale

if __name__ == "__main__":
    palette = Palette(50, (0, 0, 0), (250, 485), 10)
    print(palette.position_x, palette.position_y)