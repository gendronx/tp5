# ^^­^^

import arcade

# Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Dessin Tp5"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

# soleil
pt = 700
points_soleil = [(630, 520), (700, 590), (770, 520), (700, 450)]
arcade.draw.draw_polygon_filled(points_soleil, arcade.color.ELECTRIC_YELLOW)

# neige/sol
arcade.draw_lrbt_rectangle_filled(
    0, SCREEN_WIDTH,
    0, SCREEN_HEIGHT / 20,
    arcade.csscolor.WHITE)

# arbre
r = arcade.rect.XYWH(100, 500, 30, 60)
arcade.draw_rect_filled(r, arcade.color.BUBBLE_GUM)


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

arcade.finish_render()

arcade.run()
