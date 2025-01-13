import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Tutoriel Arcade"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
arcade.draw.draw_lrbt_rectangle_filled(
    0, SCREEN_WIDTH,
    0, SCREEN_HEIGHT / 2,
    arcade.csscolor.DARK_GREEN)
r = arcade.rect.XYWH(200, SCREEN_HEIGHT / 2, 30, 60)
arcade.draw.draw_rect_filled(r, arcade.csscolor.BROWN)
arcade.finish_render()

arcade.run()
