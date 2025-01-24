"""
Xavier Gendron
groupe 404
Ce programme crée un dessin avec arcade
"""

import arcade


# Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Dessin Tp5"


def on_draw():
    arcade.start_render()

    # soleil
    points_soleil = [(630, 520), (700, 590), (770, 520), (700, 450)]
    arcade.draw.draw_polygon_filled(points_soleil, arcade.color.ELECTRIC_YELLOW)

    # neige/sol
    arcade.draw_lrbt_rectangle_filled(
        0, SCREEN_WIDTH,
        0, SCREEN_HEIGHT / 20 + 10,
        arcade.csscolor.WHITE)

    # arbre1
    r = arcade.rect.XYWH(120, 357, 30, 60)
    arcade.draw_rect_filled(r, arcade.color.BLACK)
    arcade.draw.draw_triangle_filled(90, 387,
                                     120, 407,
                                     150, 387,
                                     arcade.color.BLACK)
    arcade.draw.draw_triangle_filled(90, 397,
                                     120, 417,
                                     150, 397,
                                     arcade.color.BLACK)
    arcade.draw.draw_triangle_filled(90, 407,
                                     120, 427,
                                     150, 407,
                                     arcade.color.BLACK)

    # arbre2
    r = arcade.rect.XYWH(200, 260, 30, 60)
    arcade.draw_rect_filled(r, arcade.color.BLACK)
    arcade.draw.draw_triangle_filled(170, 290,
                                     200, 310,
                                     230, 290,
                                     arcade.color.BLACK)
    arcade.draw.draw_triangle_filled(170, 300,
                                     200, 320,
                                     230, 300,
                                     arcade.color.BLACK)
    arcade.draw.draw_triangle_filled(170, 310,
                                     200, 330,
                                     230, 310,
                                     arcade.color.BLACK)

    # arbre3
    r = arcade.rect.XYWH(350, 100, 30, 60)
    arcade.draw_rect_filled(r, arcade.color.BLACK)
    arcade.draw.draw_triangle_filled(320, 130,
                                     350, 160,
                                     380, 130,
                                     arcade.color.BLACK)
    arcade.draw.draw_triangle_filled(320, 140,
                                     350, 170,
                                     380, 140,
                                     arcade.color.BLACK)
    arcade.draw.draw_triangle_filled(320, 150,
                                     350, 180,
                                     380, 150,
                                     arcade.color.BLACK)

    # montagne enneigée
    arcade.draw.draw_triangle_filled(0, 500,
                                     400, 30,
                                     0, 30,
                                     arcade.color.SNOW)
    # nuage1
    arcade.draw.draw_circle_filled(300, 500, 30, arcade.color.ANTI_FLASH_WHITE)
    arcade.draw.draw_circle_filled(330, 500, 30, arcade.color.ANTI_FLASH_WHITE)
    arcade.draw.draw_circle_filled(360, 500, 30, arcade.color.ANTI_FLASH_WHITE)
    arcade.draw.draw_circle_filled(390, 500, 30, arcade.color.ANTI_FLASH_WHITE)
    arcade.draw.draw_circle_filled(420, 500, 30, arcade.color.ANTI_FLASH_WHITE)

    # nuage2
    arcade.draw.draw_circle_filled(480, 450, 30, arcade.color.ANTI_FLASH_WHITE)
    arcade.draw.draw_circle_filled(510, 450, 30, arcade.color.ANTI_FLASH_WHITE)
    arcade.draw.draw_circle_filled(540, 450, 30, arcade.color.ANTI_FLASH_WHITE)

    # cadre
    line_list = [(0, 0), (800, 0), (800, 0), (800, 600), (800, 600), (0, 600), (0, 600), (0, 0)]
    arcade.draw.draw_lines(line_list, arcade.color.BLACK, line_width=50)

    line_list = [(15, 15), (785, 15), (785, 15), (785, 585), (785, 585), (15, 585), (15, 585), (15, 15)]
    arcade.draw.draw_lines(line_list, arcade.color.WHITE, line_width=1)

    # texte
    affichage = arcade.Text("HIVER 2077", 350, 550, arcade.color.BRITISH_RACING_GREEN, font_size=20)
    affichage.draw()

    # equipement ski
    arcade.draw_lrbt_rectangle_filled(
        500, SCREEN_WIDTH - 50,
        40, 150,
        arcade.csscolor.BEIGE)

    arcade.draw.draw_arc_filled(625, 150, 250, 100, arcade.csscolor.INDIANRED, 0, 180)

    # porte
    r = arcade.rect.XYWH(525, 70, 30, 60)
    arcade.draw_rect_filled(r, arcade.color.WOOD_BROWN)

    arcade.draw.draw_arc_filled(525, 100, 30, 20, arcade.csscolor.PALE_VIOLET_RED, 0, 180)

    arcade.draw.draw_circle_filled(520, 70, 4, arcade.color.BLACK)

    # panneau
    arcade.draw.draw_ellipse_filled(625, 130, 40, 80, arcade.color.FOREST_GREEN, tilt_angle=90)

    affichage = arcade.Text("Équipement", 593, 127, arcade.color.BRITISH_RACING_GREEN, font_size=10)
    affichage.draw()

    affichage = arcade.Text("SKI", 600, 80, arcade.color.DARK_ORANGE, font_size=20)
    affichage.draw()

    # fenetre
    arcade.draw.draw_circle_filled(675, 90, 15, arcade.color.LIGHT_SKY_BLUE)
    line_list = [(660, 90), (690, 90), (675, 75), (675, 105)]
    arcade.draw.draw_lines(line_list, arcade.color.WHITE, line_width=1)

    arcade.finish_render()


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

    arcade.set_background_color(arcade.color.SKY_BLUE)
    on_draw()
    arcade.run()


main()
