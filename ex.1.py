#^^­^^

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Tutoriel Arcade"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
#gazon
arcade.draw.draw_lrbt_rectangle_filled(
    0, SCREEN_WIDTH,
    0, SCREEN_HEIGHT / 2,
    arcade.csscolor.DARK_GREEN)

#soleil
pt = 700
points_soleil = [(630, 520), (700, 590), (770, 520), (700, 450)]
arcade.draw.draw_polygon_filled(points_soleil, arcade.color.ELECTRIC_YELLOW)
#arcade.draw.draw_circle_filled(700, SCREEN_HEIGHT - 80, 70, arcade.color.ELECTRIC_YELLOW)

#arbre1
r = arcade.rect.XYWH(200, SCREEN_HEIGHT / 2, 30, 60)
arcade.draw.draw_rect_filled(r, arcade.csscolor.BROWN)
arcade.draw.draw_circle_filled(200, SCREEN_HEIGHT / 2 + 20, 30, arcade.color.FOREST_GREEN)

#arbre2
r2 = arcade.rect.XYWH(300, SCREEN_HEIGHT / 2, 30, 60)
arcade.draw.draw_rect_filled(r2, arcade.csscolor.BROWN)
arcade.draw.draw_ellipse_filled(300, SCREEN_HEIGHT / 2 + 60, 60, 100, arcade.color.FOREST_GREEN)

#arbre3
r3 = arcade.rect.XYWH(400, SCREEN_HEIGHT / 2, 30, 60)
arcade.draw.draw_rect_filled(r3, arcade.csscolor.BROWN)
arcade.draw.draw_arc_filled(400, SCREEN_HEIGHT / 2 + 20, 60, 100, arcade.csscolor.FOREST_GREEN, 0, 180)

#arbre4
r4 = arcade.rect.XYWH(500, SCREEN_HEIGHT / 2, 30, 60)
arcade.draw.draw_rect_filled(r4, arcade.csscolor.BROWN)
y = SCREEN_HEIGHT / 2 + 40
arcade.draw.draw_triangle_filled(500, y + 40,
                                 470, y - 20,
                                 530, y - 20,
                                 arcade.color.FOREST_GREEN)

#arbre5
r5 = arcade.rect.XYWH(600, SCREEN_HEIGHT / 2, 30, 60)
arcade.draw.draw_rect_filled(r5, arcade.csscolor.BROWN)
affichage = arcade.Text("Arbre", 580, SCREEN_HEIGHT / 2 + 45, arcade.color.FOREST_GREEN)
affichage.draw()


#arcade.draw.draw_line(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 110, SCREEN_WIDTH, SCREEN_HEIGHT - 110, arcade.color.BANANA_YELLOW, 10)
#points = [(700, 300), (750, 600), (345, 675)]
#arcade.draw.draw_line_strip(points, arcade.color.BUFF)
#line_list = [(139, 556), (720, 512), (773, 704), (710, 596)]
#arcade.draw.draw_lines(line_list, arcade.color.FOREST_GREEN)
#points2 = [(700, 300), (750, 600), (345, 675)]
#arcade.draw.draw_polygon_filled(points2, arcade.color.AERO_BLUE)
#points3 = [(200, 200), (350, 200), (345, 375), (23, 224), (222, 222)]
#arcade.draw.draw_polygon_outline(points3, arcade.color.ALIZARIN_CRIMSON, 10)

arcade.finish_render()

arcade.run()
