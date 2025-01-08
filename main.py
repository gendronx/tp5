import arcade
import random


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        self.clear()
        for i in range(20):
            liste_couleur = [arcade.color.CLASSIC_ROSE, arcade.color.DARK_LAVA, arcade.color.GLITTER, arcade.color.FRENCH_BISTRE, arcade.color.AIR_SUPERIORITY_BLUE, arcade.color.ALABAMA_CRIMSON, arcade.color.INCHWORM]
            color = random.choice(liste_couleur)
            x = random.randint(20, 620)
            y = random.randint(20, 460)
            arcade.draw_circle_filled(x, y, 20, color)


def main():

    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
